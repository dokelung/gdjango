# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_collaborator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='department',
            field=models.CharField(max_length=40),
        ),
    ]
