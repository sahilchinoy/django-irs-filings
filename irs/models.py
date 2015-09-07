from django.db import models


class Committee(models.Model):
    """
    A political committee that files disclosure reports with
    the IRS under section 527 of the U.S. tax code.
    """

    EIN = models.CharField(
        primary_key=True,
        max_length=9)
    name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.name


class Contribution(models.Model):
    """
    An itemization on Schedule A of a Form 8872 report.
    """

    record_type = models.CharField(max_length=1)
    form_id_number = models.CharField(max_length=38)
    schedule_a_id = models.CharField(max_length=38)
    organization_name = models.CharField(max_length=70)
    EIN = models.CharField(max_length=9)
    contributor_name = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    contributor_address_line_1 = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    contributor_address_line_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    contributor_address_city = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    contributor_address_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    contributor_address_zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True)
    contributor_address_zip_ext = models.CharField(
        max_length=4,
        null=True,
        blank=True)
    contributor_employer = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    contribution_amount = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        null=True)
    contributor_occupation = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    agg_contribution_ytd = models.DecimalField(
        null=True,
        max_digits=17,
        decimal_places=2)
    contribution_date = models.DateField(
        auto_now=False,
        null=True)
    filing = models.ForeignKey(
        'F8872',
        null=True,
        related_name='contributions')
    committee = models.ForeignKey(
        'Committee',
        null=True,
        related_name='contributions')

    # For probabilistic people parsing
    entity_type = models.CharField(
        max_length=20,
        null=True,
        blank=True)
    contributor_first_name = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    contributor_last_name = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    contributor_middle_name = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    contributor_corporation_name = models.CharField(
        max_length=70,
        null=True,
        blank=True)

    def __unicode__(self):
        return self.contributor_name


class Expenditure(models.Model):
    """
    An itemization on Schedule B of a Form 8872 report.
    """

    record_type = models.CharField(max_length=1)
    form_id_number = models.CharField(max_length=38)
    schedule_b_id = models.CharField(max_length=38)
    organization_name = models.CharField(max_length=70)
    EIN = models.CharField(max_length=9)
    recipient_name = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    recipient_address_line_1 = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    recipient_address_line_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    recipient_address_city = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    recipient_address_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    recipient_address_zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True)
    recipient_address_zip_ext = models.CharField(
        max_length=4,
        null=True,
        blank=True)
    recipient_employer = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    expenditure_amount = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        null=True)
    recipient_occupation = models.CharField(
        max_length=70,
        null=True,
        blank=True)
    expenditure_date = models.DateField(
        auto_now=False,
        null=True)
    expenditure_purpose = models.CharField(
        max_length=512,
        null=True,
        blank=True)
    filing = models.ForeignKey(
        'F8872',
        null=True,
        related_name='expenditures')
    committee = models.ForeignKey(
        'Committee',
        null=True,
        related_name='expenditures')

    def __unicode__(self):
        return self.recipient_name


class F8872(models.Model):
    """
    A quarterly, midyear or end-of-year report of contributions and
    expenditures for a political committee.
    """

    committee = models.ForeignKey(
        'Committee',
        null=True,
        related_name='filings')
    record_type = models.CharField(max_length=1)
    form_type = models.IntegerField()
    form_id_number = models.CharField(
        primary_key=True,
        max_length=38)
    begin_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    initial_report_indicator = models.IntegerField(null=True)
    amended_report_indicator = models.IntegerField(null=True)
    final_report_indicator = models.IntegerField(null=True)
    change_of_address_indicator = models.IntegerField(null=True)
    organization_name = models.CharField(max_length=70)
    EIN = models.CharField(max_length=9)
    mailing_address_line_1 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    mailing_address_line_2 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    mailing_address_city = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    mailing_address_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    mailing_address_zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True)
    mailing_address_zip_ext = models.CharField(
        max_length=4,
        null=True,
        blank=True)
    email = models.CharField(
        max_length=150,
        null=True,
        blank=True)
    org_formation_date = models.DateField(
        auto_now=False,
        null=True)
    custodian_name = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    custodian_address_line_1 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    custodian_address_line_2 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    custodian_address_city = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    custodian_address_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    custodian_address_zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True)
    custodian_address_zip_ext = models.CharField(
        max_length=4,
        null=True,
        blank=True)
    contact_name = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    contact_address_line_1 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    contact_address_line_2 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    contact_address_city = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    contact_address_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    contact_address_zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True)
    contact_address_zip_ext = models.CharField(
        max_length=4,
        null=True,
        blank=True)
    business_address_line_1 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    business_address_line_2 = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    business_address_city = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    business_address_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    business_address_zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True)
    business_address_zip_ext = models.CharField(
        max_length=4,
        null=True,
        blank=True)
    quarter_indicator = models.IntegerField(null=True)
    monthly_report_month = models.IntegerField(null=True)
    pre_election_type = models.CharField(
        max_length=10,
        null=True,
        blank=True)
    election_date = models.DateField(
        auto_now=False,
        null=True)
    election_state = models.CharField(
        max_length=2,
        null=True,
        blank=True)
    schedule_a_indicator = models.IntegerField(null=True)
    schedule_a_total = models.DecimalField(
        max_digits=17,
        decimal_places=2)
    schedule_b_indicator = models.IntegerField(null=True)
    schedule_b_total = models.DecimalField(
        max_digits=17,
        decimal_places=2)
    insert_datetime = models.DateTimeField(auto_now=False)

    is_amended = models.BooleanField(default=False)
    amended_by = models.ForeignKey(
        'self',
        null=True,
        related_name='amends')

    class Meta:
        ordering = ['-end_date', '-form_id_number']

    def __unicode__(self):
        return self.form_id_number
