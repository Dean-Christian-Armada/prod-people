# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0018_emergencycontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detained',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detained', models.NullBooleanField(default=None)),
                ('reason', models.ForeignKey(default=None, to='mariners_profile.Reasons')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DisciplinaryAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplinary_action', models.NullBooleanField(default=None)),
                ('reason', models.ForeignKey(default=None, to='mariners_profile.Reasons')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisaApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visa_application', models.NullBooleanField(default=None)),
                ('reason', models.ForeignKey(default=None, to='mariners_profile.Reasons')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
