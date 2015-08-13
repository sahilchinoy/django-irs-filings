import os
import csv
import string
from datetime import *

from django.conf import settings
from django.core.management.base import BaseCommand

from irs.models import *

f8872 = (
	'record_type',
	'form_type',
	'form_id_number',
	'begin_date',
	'end_date',
	'initial_report_indicator',
	'amended_report_indicator',
	'final_report_indicator',
	'change_of_address_indicator',
	'organization_name',
	'EIN',
	'mailing_address_line_1',
	'mailing_address_line_2',
	'mailing_address_city',
	'mailing_address_state',
	'mailing_address_zip_code',
	'mailing_address_zip_ext',
	'email',
	'org_formation_date',
	'custodian_name',
	'custodian_address_line_1',
	'custodian_address_line_2',
	'custodian_address_city',
	'custodian_address_state',
	'custodian_address_zip_code',
	'custodian_address_zip_ext',
	'contact_name',
	'contact_address_line_1',
	'contact_address_line_2',
	'contact_address_city',
	'contact_address_state',
	'contact_address_zip_code',
	'contact_address_zip_ext',
	'business_address_line_1',
	'business_address_line_2',
	'business_address_city',
	'business_address_state',
	'business_address_zip_code',
	'business_address_zip_ext',
	'quarter_indicator',
	'monthly_report_month',
	'pre_election_type',
	'election_date',
	'election_state',
	'schedule_a_indicator',
	'schedule_a_total',
	'schedule_b_indicator',
	'schedule_b_total',
	'insert_datetime'
	)

sa = (
	'record_type',
	'form_id_number',
	'schedule_a_id',
	'organization_name',
	'EIN',
	'contributor_name',
	'contributor_address_line_1',
	'contributor_address_line_2',
	'contributor_city',
	'contributor_state',
	'contributor_zip',
	'contributor_zip_ext',
	'contributor_employer',
	'contribution_amount',
	'contributor_occupation',
	'contribution_ytd',
	'contribution_date'
	)

def create_8872(row):
	obj = {}
	table = string.maketrans("","")
	for i, cell in enumerate(row[0:49]):
		# some cleanup
		cell.translate(table, string.punctuation)

		# date rows
		if i in [3,4,18,42] and cell:
			cell = datetime.strptime(cell, '%Y%m%d')
		# nullable integer rows
		elif i in [40,41]:
			try:
				cell = int(cell)
			except ValueError:
				cell = None

		if not cell:
			cell = None

		obj[f8872[i]] = cell

	filing = F8872(**obj)
	return filing

class Command(BaseCommand):
	def handle(self, *args, **options):
		F8872.objects.all().delete()

		path = os.path.join(settings.BASE_DIR,'irs','data','FullDataFile.txt')
		print path
		with open(path,'r') as raw_file:
			reader = csv.reader(raw_file, delimiter='|')
			bulk_filings = []
			for row in reader:
				try:
					if row[0] == '2':
						filing = create_8872(row)
						bulk_filings.append(filing)
						print 'Created filing'
				except IndexError:
					pass

			print('Creating {} filings'.format(len(bulk_filings)))
			F8872.objects.bulk_create(bulk_filings, batch_size=1000)