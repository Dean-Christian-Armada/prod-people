# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fields',
            name='slug',
        ),
    ]
