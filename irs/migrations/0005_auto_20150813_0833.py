# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0004_auto_20150813_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8872',
            name='election_state',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
    ]
