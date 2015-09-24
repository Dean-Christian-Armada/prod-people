# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0074_auto_20150924_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NegativeHealthProblems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health_problems', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NegativeSeagoingHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seagoing_comments', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PersonReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_reference', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=None)),
                ('veracity_seagoing_history', models.NullBooleanField()),
                ('health_problem', models.NullBooleanField()),
                ('financial_liability', models.NullBooleanField()),
                ('rehiring_prospects', models.NullBooleanField()),
                ('character', models.TextField(default=None, null=True, blank=True)),
                ('comments', models.TextField(default=None, null=True, blank=True)),
                ('company', models.ForeignKey(default=None, to='mariners_profile.Company')),
                ('person_contacted', models.ForeignKey(default=None, to='mariners_profile.PersonReference')),
                ('user', models.ForeignKey(related_name='user_mariner', default=None, to='login.UserProfile')),
                ('verified_by', models.ForeignKey(related_name='verified_by', default=None, to='login.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='marinersprofile',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 9, 44, 39, 139181, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
