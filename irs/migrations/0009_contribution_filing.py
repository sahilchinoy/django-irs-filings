# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0008_contribution_contributor_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='filing',
            field=models.ForeignKey(to='irs.F8872', null=True),
        ),
    ]
