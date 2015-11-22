# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20151119_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filefieldvalue',
            options={'ordering': ['field']},
        ),
    ]
