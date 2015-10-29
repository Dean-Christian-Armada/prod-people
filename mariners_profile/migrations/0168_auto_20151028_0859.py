# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0167_auto_20151026_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotee',
            name='allotee_first_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allotee',
            name='allotee_last_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allotee',
            name='allotee_middle_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allotee',
            name='allotee_relationship',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Relationship'),
        ),
        migrations.AlterField(
            model_name='allotee',
            name='allotee_zip',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Zip'),
        ),
        migrations.AlterField(
            model_name='allotee',
            name='bank',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Bank'),
        ),
    ]
