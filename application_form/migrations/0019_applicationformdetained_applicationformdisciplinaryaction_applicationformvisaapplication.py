# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0018_emergencycontact'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0018_applicationformemergencycontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormDetained',
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
            name='ApplicationFormDisciplinaryAction',
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
            name='ApplicationFormVisaApplication',
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
