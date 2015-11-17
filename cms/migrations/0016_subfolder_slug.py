# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20151113_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='subfolder',
            name='slug',
            field=models.SlugField(default=None, null=True, blank=True),
        ),
    ]
