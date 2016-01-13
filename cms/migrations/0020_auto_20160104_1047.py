# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0019_auto_20151124_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subfolder',
            name='slug',
            field=models.SlugField(null=True, default=None, max_length=100, blank=True),
        ),
    ]
