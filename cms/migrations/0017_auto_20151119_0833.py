# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_subfolder_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fields',
            options={'ordering': ['order']},
        ),
    ]
