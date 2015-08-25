# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irs', '0017_auto_20150820_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='f8872',
            name='is_amended',
            field=models.BooleanField(default=False),
        ),
    ]
