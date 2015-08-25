# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0016_auto_20150819_0610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='f8872',
            options={'ordering': ['-form_id_number']},
        ),
        migrations.AddField(
            model_name='f8872',
            name='amended_by',
            field=models.ForeignKey(related_name='amends', to='irs.F8872', null=True),
        ),
    ]
