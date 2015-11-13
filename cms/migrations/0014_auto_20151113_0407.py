# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_fields_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='slug',
            field=models.SlugField(default=None, null=True, blank=True),
        ),
    ]
