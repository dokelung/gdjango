# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('link', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('thesis', models.CharField(max_length=20)),
                ('thesis_chinese', models.CharField(max_length=20)),
                ('gyear', models.CharField(max_length=4)),
                ('degree', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
