# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0022_auto_20150830_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='agg_contribution_ytd',
            field=models.DecimalField(null=True, max_digits=17, decimal_places=2),
        ),
    ]
