# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0010_auto_20150816_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8872',
            name='custodian_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='email',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='org_formation_date',
            field=models.DateField(null=True),
        ),
    ]
