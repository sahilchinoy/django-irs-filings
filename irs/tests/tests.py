from django.test import TestCase
from django.core.management import call_command
from irs.models import F8872, Contribution, Expenditure, Committee


class IRSFilingsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup the test database by loading a subset of a
        real filing.
        """
        call_command('loadIRS', test=True, verbose=True)

    def test_load_command(self):
        """
        Check if all the models were loaded.
        """
        self.assertEqual(
            F8872.objects.count(),
            65)
        self.assertEqual(
            Contribution.objects.count(),
            5911)
        self.assertEqual(
            Expenditure.objects.count(),
            5068)
        self.assertEqual(
            Committee.objects.count(),
            49)

    def test_committee(self):
        """
        Check if the committees are being associated
        with their filings correctly.
        """
        committee = Committee.objects.get(EIN='751954937')
        self.assertEqual(
            committee.name,
            'GARDERE WYNNE SEWELL L L P CAMPAIGN FUND')
        self.assertEqual(
            committee.filings.count(),
            3)

    def test_contributions(self):
        """
        Check if all the contributions and their totals are being
        loaded correctly.
        """
        filing = F8872.objects.get(form_id_number='9637673')
        contributions_list = filing.contributions.values_list(
            'contribution_amount',
            flat=True)
        sum_contributions = sum(a for a in contributions_list)
        self.assertEqual(
            sum_contributions,
            filing.schedule_a_total)

    def test_amendments(self):
        """
        Check if amendments are being resolved correctly.
        """
        filing = F8872.objects.get(form_id_number='9637689')
        self.assertEqual(
            filing.amends.first().form_id_number,
            '9637644'
            )
        amended_filing = F8872.objects.get(form_id_number='9637644')
        self.assertTrue(amended_filing.is_amended)
        self.assertEqual(
            amended_filing.amended_by.form_id_number,
            '9637689'
            )

    @classmethod
    def tearDownClass(cls):
        pass
