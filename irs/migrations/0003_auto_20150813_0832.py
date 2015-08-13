# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0002_auto_20150813_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8872',
            name='business_address_line_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='contact_address_line_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='custodian_address_line_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='election_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='mailing_address_line_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
