# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='F8872',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_type', models.CharField(max_length=1)),
                ('form_type', models.IntegerField()),
                ('form_id_number', models.CharField(max_length=38)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('initial_report_indicator', models.IntegerField()),
                ('amended_report_indicator', models.IntegerField()),
                ('final_report_indicator', models.IntegerField()),
                ('change_of_address_indicator', models.IntegerField()),
                ('organization_name', models.CharField(max_length=70)),
                ('EIN', models.CharField(max_length=9)),
                ('mailing_address_line_1', models.CharField(max_length=50)),
                ('mailing_address_line_2', models.CharField(max_length=50)),
                ('mailing_address_city', models.CharField(max_length=50)),
                ('mailing_address_state', models.CharField(max_length=2)),
                ('mailing_address_zip_code', models.CharField(max_length=5)),
                ('mailing_address_zip_ext', models.CharField(max_length=4)),
                ('email', models.CharField(max_length=150)),
                ('org_formation_date', models.DateField()),
                ('custodian_name', models.CharField(max_length=50)),
                ('custodian_address_line_1', models.CharField(max_length=50)),
                ('custodian_address_line_2', models.CharField(max_length=50)),
                ('custodian_address_city', models.CharField(max_length=50)),
                ('custodian_address_state', models.CharField(max_length=2)),
                ('custodian_address_zip_code', models.CharField(max_length=5)),
                ('custodian_address_zip_ext', models.CharField(max_length=4)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_address_line_1', models.CharField(max_length=50)),
                ('contact_address_line_2', models.CharField(max_length=50)),
                ('contact_address_city', models.CharField(max_length=50)),
                ('contact_address_state', models.CharField(max_length=2)),
                ('contact_address_zip_code', models.CharField(max_length=5)),
                ('contact_address_zip_ext', models.CharField(max_length=4)),
                ('business_address_line_1', models.CharField(max_length=50)),
                ('business_address_line_2', models.CharField(max_length=50)),
                ('business_address_city', models.CharField(max_length=50)),
                ('business_address_state', models.CharField(max_length=2)),
                ('business_address_zip_code', models.CharField(max_length=5)),
                ('business_address_zip_ext', models.CharField(max_length=4)),
                ('quarter_indicator', models.IntegerField()),
                ('monthly_report_month', models.IntegerField(null=True)),
                ('pre_elect_type', models.IntegerField(null=True)),
                ('election_date', models.DateField()),
                ('election_state', models.CharField(max_length=2)),
                ('schedule_a_indicator', models.IntegerField()),
                ('total_schedule_a', models.DecimalField(max_digits=10, decimal_places=2)),
                ('schedule_b_indicator', models.IntegerField()),
                ('total_schedule_b', models.DecimalField(max_digits=10, decimal_places=2)),
                ('insert_datetime', models.DateTimeField()),
            ],
        ),
    ]
