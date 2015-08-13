# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='f8872',
            old_name='pre_elect_type',
            new_name='pre_election_type',
        ),
        migrations.RenameField(
            model_name='f8872',
            old_name='total_schedule_a',
            new_name='schedule_a_total',
        ),
        migrations.RenameField(
            model_name='f8872',
            old_name='total_schedule_b',
            new_name='schedule_b_total',
        ),
        migrations.AlterField(
            model_name='f8872',
            name='form_id_number',
            field=models.CharField(max_length=38, db_index=True),
        ),
    ]
