# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0012_auto_20150816_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='contributor_corporation_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contribution',
            name='contributor_middle_initial',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='entity_type',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
