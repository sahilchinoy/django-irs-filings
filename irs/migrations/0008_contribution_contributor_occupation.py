# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0007_auto_20150816_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='contributor_occupation',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
