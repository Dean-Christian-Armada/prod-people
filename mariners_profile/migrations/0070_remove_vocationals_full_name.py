# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0069_auto_20150923_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocationals',
            name='full_name',
        ),
    ]
