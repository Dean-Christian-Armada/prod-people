# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0023_auto_20150908_0633'),
        ('application_form', '0023_auto_20150908_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormCOC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coc', models.CharField(default=None, unique=True, max_length=100)),
                ('coc_expiry', models.DateField(default=None)),
                ('rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormGOC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goc', models.CharField(default=None, unique=True, max_length=100)),
                ('goc_expiry', models.DateField(default=None)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormLicense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.CharField(default=None, unique=True, max_length=100)),
                ('license_expiry', models.DateField(default=None)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormSbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sbook', models.CharField(default=None, unique=True, max_length=100)),
                ('sbook_expiry', models.DateField(default=None)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormSchengenVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schengen_visa', models.CharField(default=None, unique=True, max_length=100)),
                ('schengen_visa_expiry', models.DateField(default=None, blank=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormSRC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src', models.CharField(default=None, unique=True, max_length=100)),
                ('src_rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormUSVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('us_visa', models.CharField(default=None, unique=True, max_length=100)),
                ('us_visa_expiry', models.DateField(default=None, blank=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFormYellowFever',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yellow_fever', models.CharField(default=None, unique=True, max_length=100)),
                ('yellow_fever_expiry', models.DateField(default=None)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
