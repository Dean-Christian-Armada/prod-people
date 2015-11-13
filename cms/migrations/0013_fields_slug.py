# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_remove_fields_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='slug',
            field=models.SlugField(null=True, default=None, blank=True, unique=True),
        ),
    ]
