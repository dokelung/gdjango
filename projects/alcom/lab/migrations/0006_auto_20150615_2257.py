# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_auto_20150614_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='first_name_chinese',
            field=models.CharField(max_length=7, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='last_name_chinese',
            field=models.CharField(max_length=5, null=True),
            preserve_default=True,
        ),
    ]
