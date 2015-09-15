# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0034_auto_20150908_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargedOffense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('charged_offense', models.NullBooleanField(default=None)),
                ('charged_offense_reason', models.ForeignKey(default=None, to='mariners_profile.Reasons')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Termination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('termination', models.NullBooleanField(default=None)),
                ('termination_reason', models.ForeignKey(default=None, to='mariners_profile.Reasons')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
