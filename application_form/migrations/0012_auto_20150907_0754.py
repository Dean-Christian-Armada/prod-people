# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0011_applicationformspouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformspouse',
            name='spouse_name',
        ),
        migrations.AddField(
            model_name='applicationformspouse',
            name='spouse_first_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformspouse',
            name='spouse_last_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformspouse',
            name='spouse_middle_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
