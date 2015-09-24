# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0066_primaryschool_vocational'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocationals',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='vocationals',
            name='vocational_name',
        ),
    ]
