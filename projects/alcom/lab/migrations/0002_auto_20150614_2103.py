# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='email',
        ),
        migrations.RemoveField(
            model_name='people',
            name='name',
        ),
        migrations.AddField(
            model_name='people',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
