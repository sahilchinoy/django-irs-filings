# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0015_auto_20150817_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('EIN', models.CharField(max_length=9, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='contribution',
            name='committee',
            field=models.ForeignKey(related_name='contributions', to='irs.Committee', null=True),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='committee',
            field=models.ForeignKey(related_name='expenditures', to='irs.Committee', null=True),
        ),
        migrations.AddField(
            model_name='f8872',
            name='committee',
            field=models.ForeignKey(related_name='filings', to='irs.Committee', null=True),
        ),
    ]
