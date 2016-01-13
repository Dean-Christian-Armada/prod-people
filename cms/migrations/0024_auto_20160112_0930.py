# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_updatefileinfolog_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='updatefileinfolog',
            options={'ordering': ['-id']},
        ),
    ]
