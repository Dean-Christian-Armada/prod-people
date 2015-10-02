# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0083_auto_20150930_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentaddress',
            name='current_street',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='currentaddress',
            name='current_unit',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='emergency_street',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='emergency_unit',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='permanent_street',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='permanent_unit',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
