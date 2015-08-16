# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0006_auto_20150813_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_type', models.CharField(max_length=1)),
                ('form_id_number', models.CharField(max_length=38)),
                ('schedule_a_id', models.CharField(max_length=38)),
                ('organization_name', models.CharField(max_length=70)),
                ('EIN', models.CharField(max_length=9)),
                ('contributor_name', models.CharField(max_length=50, null=True, blank=True)),
                ('contributor_address_line_1', models.CharField(max_length=50, null=True, blank=True)),
                ('contributor_address_line_2', models.CharField(max_length=50, null=True, blank=True)),
                ('contributor_address_city', models.CharField(max_length=50, null=True, blank=True)),
                ('contributor_address_state', models.CharField(max_length=50, null=True, blank=True)),
                ('contributor_address_zip_code', models.CharField(max_length=5, null=True, blank=True)),
                ('contributor_address_zip_ext', models.CharField(max_length=4, null=True, blank=True)),
                ('contributor_employer', models.CharField(max_length=70, null=True, blank=True)),
                ('contribution_amount', models.DecimalField(max_digits=17, decimal_places=2)),
                ('agg_contribution_ytd', models.DecimalField(max_digits=17, decimal_places=2)),
                ('contribution_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='f8872',
            name='id',
        ),
        migrations.AlterField(
            model_name='f8872',
            name='form_id_number',
            field=models.CharField(max_length=38, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='schedule_a_total',
            field=models.DecimalField(max_digits=17, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='schedule_b_total',
            field=models.DecimalField(max_digits=17, decimal_places=2),
        ),
    ]
