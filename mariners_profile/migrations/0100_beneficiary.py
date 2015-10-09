# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0099_auto_20151009_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beneficiary_first_name', models.CharField(default=None, max_length=50, null=True)),
                ('beneficiary_middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('beneficiary_last_name', models.CharField(default=None, max_length=50, null=True)),
                ('beneficiary_number', models.BigIntegerField(default=None, null=True, blank=True)),
                ('relationship', models.ForeignKey(default=None, to='mariners_profile.Relationship')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
    ]
