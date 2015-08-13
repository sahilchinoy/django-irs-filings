# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0003_auto_20150813_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8872',
            name='business_address_zip_ext',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='contact_address_zip_ext',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='custodian_address_zip_ext',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='mailing_address_zip_ext',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
