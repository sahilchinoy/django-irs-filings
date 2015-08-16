# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0009_contribution_filing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='contribution_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='filing',
            field=models.ForeignKey(related_name='contributions', to='irs.F8872', null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='amended_report_indicator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='change_of_address_indicator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='final_report_indicator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='initial_report_indicator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='quarter_indicator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='schedule_a_indicator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='f8872',
            name='schedule_b_indicator',
            field=models.IntegerField(null=True),
        ),
    ]
