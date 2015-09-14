# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_people_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='link',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
