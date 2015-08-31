# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0019_auto_20150828_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='contribution_amount',
            field=models.DecimalField(null=True, max_digits=17, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='expenditure_amount',
            field=models.DecimalField(null=True, max_digits=17, decimal_places=2),
        ),
    ]
