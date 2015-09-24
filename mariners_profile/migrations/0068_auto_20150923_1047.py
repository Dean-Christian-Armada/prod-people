# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0067_auto_20150923_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocational',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vocational',
            name='vocational',
        ),
        migrations.RemoveField(
            model_name='vocational',
            name='vocationalyear_from',
        ),
        migrations.RemoveField(
            model_name='vocational',
            name='vocationalyear_to',
        ),
    ]
