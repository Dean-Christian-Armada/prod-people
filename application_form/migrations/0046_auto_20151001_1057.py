# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0045_auto_20150923_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcurrentaddress',
            name='current_street',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformcurrentaddress',
            name='current_unit',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformemergencycontact',
            name='emergency_street',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformemergencycontact',
            name='emergency_unit',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformpermanentaddress',
            name='permanent_street',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformpermanentaddress',
            name='permanent_unit',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
