# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0101_auto_20151009_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landemployment',
            name='contact_first_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='contact_last_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='contact_middle_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='employer_first_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='employer_last_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='employer_middle_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
