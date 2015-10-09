# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0102_auto_20151009_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allotee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allotee_first_name', models.CharField(default=None, max_length=50, null=True)),
                ('allotee_middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('allotee_last_name', models.CharField(default=None, max_length=50, null=True)),
                ('allotee_number', models.BigIntegerField(default=None, null=True, blank=True)),
                ('allotee_unit', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('allotee_street', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('allotment_account_number', models.BigIntegerField(default=None, null=True, blank=True)),
                ('allotee_zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
                ('bank', models.ForeignKey(default=None, to='mariners_profile.Bank')),
                ('relationship', models.ForeignKey(default=None, to='mariners_profile.Relationship')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
    ]
