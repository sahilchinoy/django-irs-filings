# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0011_auto_20150816_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='contributor_first_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contribution',
            name='contributor_last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contribution',
            name='entity_type',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
    ]
