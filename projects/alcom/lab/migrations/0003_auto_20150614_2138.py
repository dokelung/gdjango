# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20150614_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='gyear',
            field=models.CharField(max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='link',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='thesis',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='thesis_chinese',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
