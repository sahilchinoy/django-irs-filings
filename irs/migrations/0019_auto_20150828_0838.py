# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0018_f8872_is_amended'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='f8872',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterField(
            model_name='contribution',
            name='contributor_name',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='recipient_name',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
