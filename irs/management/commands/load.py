import os
import csv
import string
import boto
from datetime import *
import probablepeople
from django.conf import settings
from django.core.management.base import BaseCommand

from irs.models import *

NULL_TERMS = [
    'N/A',
    'NOT APPLICABLE',
    'NA',
    'NONE',
    'NOT APPLICABE',
    'NOT APLICABLE',
    'N A',
    'N-A']

FILINGS = []
CONTRIBUTIONS = []
EXPENDITURES = []

class RowParser:
    """
    Takes a row from the raw data and a mapping of field
    positions to field names in order to clean and save the
    row to the database.
    """

    def __init__(self, form_type, mapping, row):
        self.form_type = form_type
        self.mapping = mapping
        self.row = row
        self.parsed_row = {}
        self.table = string.maketrans("","")

        self.parse_row()
        self.create_object()

    def clean_cell(self, cell, cell_type):
        """
        Uses the type of field (from the mapping) to
        determine how to clean and format the cell.
        """

        try:
            if cell_type == 'D':
                cell = datetime.strptime(cell, '%Y%m%d')
            elif cell_type == 'I':
                cell = int(cell)
            else:
                cell.translate(self.table, string.punctuation)
                cell = cell.upper()

                if not cell or cell in NULL_TERMS:
                    cell = None

        except ValueError:
            cell = None

        return cell

    def parse_row(self):
        """
        Parses a row, cell-by-cell, returning a dict of field names
        to the cleaned field values.
        """
        fields = self.mapping
        for i, cell in enumerate(self.row[0:len(fields)]):
            field_name, field_type = fields[str(i)]
            parsed_cell = self.clean_cell(cell, field_type)
            self.parsed_row[field_name] = parsed_cell

        print self.parsed_row

    def create_contribution(self):
        contribution = Contribution(**self.parsed_row)
        contribution.filing_id = contribution.form_id_number
        contribution.committee_id = contribution.EIN

        if contribution.contributor_name:
            try:
                parsed_name, entity_type = probablepeople.tag(
                    contribution.contributor_name)
                if entity_type == 'Person':
                    contribution.entity_type = 'IND'
                    first_name_or_initial = parsed_name.get('GivenName') or parsed_name.get('FirstInitial')
                    contribution.contributor_first_name = first_name_or_initial
                    middle_initial = parsed_name.get('MiddleInitial')
                    if middle_initial:
                        contribution.contributor_middle_initial = middle_initial.strip('.')
                    contribution.contributor_last_name = parsed_name.get('Surname')
                elif entity_type == 'Corporation':
                    contribution.entity_type = 'CORP'
                    contribution.contributor_corporation_name = parsed_name.get('CorporationName')

            except probablepeople.RepeatedLabelError:
                pass
        contribution.save()

    def create_object(self):
        if self.form_type == 'A':
            self.create_contribution()
            #CONTRIBUTIONS.append(contribution)
        elif self.form_type == 'B':
            expenditure = Expenditure(**self.parsed_row)
            expenditure.filing_id = expenditure.form_id_number
            expenditure.committee_id = expenditure.EIN
            #EXPENDITURES.append(expenditure)
            expenditure.save()
        elif self.form_type == '2':
            filing = F8872(**self.parsed_row)

            committee, created = Committee.objects.get_or_create(EIN=filing.EIN)
            if created:
                committee.name = filing.organization_name
                committee.save()

            filing.committee = committee

            filing.save()
        
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.build_mappings()

        print 'Flushing database'

        F8872.objects.all().delete()
        Contribution.objects.all().delete()
        Expenditure.objects.all().delete()
        Committee.objects.all().delete()

        print 'Fetching latest archive'

        c = boto.s3.connect_to_region('us-west-1')
        b = c.get_bucket('irs-itemizer')

        files = [(key, key.name)
            for key in b.list()
            if key.name.startswith('FullDataFile')]
        latest = sorted(
            files,
            key=lambda tup: tup[1].split('-')[1],
            reverse=True)[0]
        latest_key = latest[0]

        latest_key.get_contents_to_filename('latest_filings.txt')

        with open('latest_filings.txt','r') as raw_file:
            reader = csv.reader(raw_file, delimiter='|')
            bulk_filings = []
            bulk_contribs = []
            for row in reader:
                try:
                    form_type = row[0]
                    if form_type == '2':
                        RowParser(form_type, self.mappings['F8872'], row)
                        print 'Created 8872' 
                    elif form_type == 'A':
                        RowParser(form_type, self.mappings['sa'], row)
                        #print 'Created contrib' 
                    elif form_type == 'B':
                        RowParser(form_type, self.mappings['sb'], row)
                        #print 'Created expenditure' 
                except IndexError:
                    pass

        """print 'Creating {} contributions'.format(len(CONTRIBUTIONS))
        Contribution.objects.bulk_create(CONTRIBUTIONS, batch_size=1000)
        print 'Creating {} expenditures'.format(len(EXPENDITURES))
        Expenditure.objects.bulk_create(EXPENDITURES, batch_size=1000)"""

        print 'Resolving amendments'
        for filing in F8872.objects.filter(amended_report_indicator=1):
            previous_filings = F8872.objects.filter(
                committee=filing.committee,
                begin_date=filing.begin_date,
                end_date=filing.end_date,
                form_id_number__lt=filing.form_id_number)

            previous_filings.update(is_amended=True, amended_by=filing)
        
    def build_mappings(self):
        """
        Uses CSV files of field names and positions for
        different filing types to load mappings into memory,
        for use in parsing different types of rows.
        """
        self.mappings = {}
        for record_type in ('sa','sb','F8872'):
            path = os.path.join(
                settings.BASE_DIR,
                'irs',
                'mappings',
                '{}.csv'.format(record_type))
            mapping = {}
            with open(path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    mapping[row['position']] = (
                        row['model_name'],
                        row['field_type'])


            self.mappings[record_type] = mapping
