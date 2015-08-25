# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0013_auto_20150816_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8872',
            name='pre_election_type',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
