# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0082_auto_20150928_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='company_standard',
            field=models.NullBooleanField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='reference',
            name='financial_liability',
            field=models.NullBooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='reference',
            name='health_problem',
            field=models.NullBooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='reference',
            name='rehiring_prospects',
            field=models.NullBooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='reference',
            name='veracity_seagoing_history',
            field=models.NullBooleanField(default=1),
        ),
    ]
