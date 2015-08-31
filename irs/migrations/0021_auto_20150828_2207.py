# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0020_auto_20150828_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='f8872',
            options={'ordering': ['-end_date', '-form_id_number']},
        ),
        migrations.AlterField(
            model_name='contribution',
            name='contributor_address_line_1',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='contributor_address_line_2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='recipient_address_line_1',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='recipient_address_line_2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
