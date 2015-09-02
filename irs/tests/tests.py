from django.test import TestCase
from django.core.management import call_command
from irs.models import *

class LoadTestCase(TestCase):
	def load(self):
		call_command('load', test=True)
	