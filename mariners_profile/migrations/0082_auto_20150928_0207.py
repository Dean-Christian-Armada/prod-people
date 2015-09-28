# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0081_auto_20150928_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='financial_liability',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='reference',
            name='health_problem',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='reference',
            name='rehiring_prospects',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='reference',
            name='veracity_seagoing_history',
            field=models.NullBooleanField(),
        ),
    ]
