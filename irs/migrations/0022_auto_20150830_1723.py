# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0021_auto_20150828_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='contributor_corporation_name',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='contributor_first_name',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='contributor_last_name',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
