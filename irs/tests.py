from django.test import TestCase
from django.core.management import call_command
from irs.models import *

class LoadTestCase(TestCase):
    def load(self):
        call_command('load', test=True)

    def test_commitee(self):
        committee = Committee.objects.get(EIN='264437423')
        self.assertEqual(committee.name, 'AMERICAN COUNCIL OF LIFE INSURERS POLITICAL ACTIVI')
