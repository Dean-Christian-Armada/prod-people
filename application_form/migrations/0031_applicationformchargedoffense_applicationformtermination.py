# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0034_auto_20150908_1219'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0030_auto_20150908_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormChargedOffense',
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
            name='ApplicationFormTermination',
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
