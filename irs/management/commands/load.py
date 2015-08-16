import os
import csv
import string
from datetime import *
import probablepeople
from django.conf import settings
from django.core.management.base import BaseCommand

from irs.models import *

sa_fields = (
	('record_type','c'),
	('form_id_number','c'),
	('schedule_a_id','c'),
	('organization_name','c'),
	('EIN','c'),
	('contributor_name','n'),
	('contributor_address_line_1','c'),
	('contributor_address_line_2','c'),
	('contributor_address_city','c'),
	('contributor_address_state','c'),
	('contributor_address_zip_code','c'),
	('contributor_address_zip_ext','c'),
	('contributor_employer','c'),
	('contribution_amount','a'),
	('contributor_occupation','c'),
	('agg_contribution_ytd','a'),
	('contribution_date','d'),
)

F8872_fields = (
	('record_type','c'),
	('form_type','c'),
	('form_id_number','c'),
	('begin_date','d'),
	('end_date','d'),
	('initial_report_indicator','c'),
	('amended_report_indicator','c'),
	('final_report_indicator','c'),
	('change_of_address_indicator','c'),
	('organization_name','c'),
	('EIN','c'),
	('mailing_address_line_1','c'),
	('mailing_address_line_2','c'),
	('mailing_address_city','c'),
	('mailing_address_state','c'),
	('mailing_address_zip_code','c'),
	('mailing_address_zip_ext','c'),
	('email','c'),
	('org_formation_date','d'),
	('custodian_name','c'),
	('custodian_address_line_1','c'),
	('custodian_address_line_2','c'),
	('custodian_address_city','c'),
	('custodian_address_state','c'),
	('custodian_address_zip_code','c'),
	('custodian_address_zip_ext','c'),
	('contact_name','c'),
	('contact_address_line_1','c'),
	('contact_address_line_2','c'),
	('contact_address_city','c'),
	('contact_address_state','c'),
	('contact_address_zip_code','c'),
	('contact_address_zip_ext','c'),
	('business_address_line_1','c'),
	('business_address_line_2','c'),
	('business_address_city','c'),
	('business_address_state','c'),
	('business_address_zip_code','c'),
	('business_address_zip_ext','c'),
	('quarter_indicator','i'),
	('monthly_report_month','i'),
	('pre_election_type','i'),
	('election_date','d'),
	('election_state','c'),
	('schedule_a_indicator','i'),
	('schedule_a_total','c'),
	('schedule_b_indicator','i'),
	('schedule_b_total','c'),
	('insert_datetime','c'),
)

class RowParser:
	def __init__(self, form_type, row):
		self.form_type = form_type
		self.row = row
		self.parsed_row = {}
		self.table = string.maketrans("","")

		self.parse_row()
		self.create_object()

	def get_mapping(self):
		if self.form_type == 'A':
			return sa_fields
		elif self.form_type == '2':
			return F8872_fields

	def clean_cell(self, cell, cell_type):
		try:
			if cell_type == 'd':
				cell = datetime.strptime(cell, '%Y%m%d')
			elif cell_type == 'i':
				cell = int(cell)
			else:
				cell.translate(self.table, string.punctuation)
				cell = cell.upper()

				if not cell or cell in ['N/A', 'NOT APPLICABLE', 'NA', 'NONE','NOT APPLICABE','NOT APLICABLE','N A','N-A']:
					cell = None

		except ValueError:
			cell = None

		return cell

	def parse_row(self):
		fields = self.get_mapping()
		for i, cell in enumerate(self.row[0:len(fields)]):
			field_name, field_type = fields[i]
			parsed_cell = self.clean_cell(cell, field_type)
			self.parsed_row[field_name] = parsed_cell

	def create_object(self):
		if self.form_type == 'A':
			contribution = Contribution(**self.parsed_row)
			contribution.filing_id = contribution.form_id_number

			if contribution.contributor_name:
				try:
					parsed_name, entity_type = probablepeople.tag(contribution.contributor_name)
					if entity_type == 'Person':
						contribution.entity_type = 'IND'
						first_name_or_initial = parsed_name.get('GivenName') or parsed_name.get('FirstInitial')

						contribution.contributor_first_name = first_name_or_initial
						contribution.contributor_middle_initial = parsed_name.get('MiddleInitial')
						contribution.contributor_last_name = parsed_name.get('Surname')
					elif entity_type == 'Corporation':
						contribution.entity_type = 'CORP'
						contribution.contributor_corporation_name = parsed_name.get('CorporationName')

				except probablepeople.RepeatedLabelError:
					pass

			contribution.save()

		elif self.form_type == '2':
			filing = F8872(**self.parsed_row)
			filing.save()


class Command(BaseCommand):
	def handle(self, *args, **options):
		F8872.objects.all().delete()
		Contribution.objects.all().delete()

		path = os.path.join(settings.BASE_DIR,'irs','data','FullDataFile.txt')
		print path
		with open(path,'r') as raw_file:
			reader = csv.reader(raw_file, delimiter='|')
			bulk_filings = []
			bulk_contribs = []
			for row in reader:
				try:
					form_type = row[0]
					if form_type == '2':
						RowParser(form_type, row)
						print 'Created 8872' 
					if form_type == 'A':
						RowParser(form_type, row)
						print 'Created contrib' 
				except IndexError:
					pass
