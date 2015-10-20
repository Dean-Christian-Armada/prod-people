# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0144_auto_20151019_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coc',
            name='coc_issuing_authority',
        ),
        migrations.RemoveField(
            model_name='ntclicense',
            name='passport_issuing_authority',
        ),
        migrations.RemoveField(
            model_name='passport',
            name='passport_issuing_authority',
        ),
        migrations.RemoveField(
            model_name='sbook',
            name='sbook_issuing_authority',
        ),
    ]
