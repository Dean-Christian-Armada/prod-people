# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20151106_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='slug',
            field=models.SlugField(null=True, default=None, blank=True, unique=True),
        ),
    ]
