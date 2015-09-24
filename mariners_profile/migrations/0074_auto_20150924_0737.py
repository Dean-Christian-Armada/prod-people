# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0073_auto_20150923_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryschool',
            name='primaryschool',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.PrimarySchools', null=True),
        ),
        migrations.AlterField(
            model_name='primaryschool',
            name='primaryschoolyear_from',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='primaryschool',
            name='primaryschoolyear_to',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='primaryschools',
            name='primaryschool_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vocational',
            name='vocational',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Vocationals', null=True),
        ),
        migrations.AlterField(
            model_name='vocational',
            name='vocationalyear_from',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vocational',
            name='vocationalyear_to',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vocationals',
            name='vocational_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
