# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0047_auto_20150910_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referrerspool',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='referrerspool',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='referrerspool',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='referrerspool',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
