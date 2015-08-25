# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0014_auto_20150817_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_type', models.CharField(max_length=1)),
                ('form_id_number', models.CharField(max_length=38)),
                ('schedule_b_id', models.CharField(max_length=38)),
                ('organization_name', models.CharField(max_length=70)),
                ('EIN', models.CharField(max_length=9)),
                ('recipient_name', models.CharField(max_length=50, null=True, blank=True)),
                ('recipient_address_line_1', models.CharField(max_length=50, null=True, blank=True)),
                ('recipient_address_line_2', models.CharField(max_length=50, null=True, blank=True)),
                ('recipient_address_city', models.CharField(max_length=50, null=True, blank=True)),
                ('recipient_address_state', models.CharField(max_length=2, null=True, blank=True)),
                ('recipient_address_zip_code', models.CharField(max_length=5, null=True, blank=True)),
                ('recipient_address_zip_ext', models.CharField(max_length=4, null=True, blank=True)),
                ('recipient_employer', models.CharField(max_length=70, null=True, blank=True)),
                ('expenditure_amount', models.DecimalField(max_digits=17, decimal_places=2)),
                ('recipient_occupation', models.CharField(max_length=70, null=True, blank=True)),
                ('expenditure_date', models.DateField(null=True)),
                ('expenditure_purpose', models.CharField(max_length=512, null=True, blank=True)),
                ('filing', models.ForeignKey(related_name='expenditures', to='irs.F8872', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contribution',
            name='contributor_address_state',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
    ]
