# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0016_auto_20150907_1156'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0016_auto_20150907_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormHighSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schoolyear_from', models.PositiveSmallIntegerField(default=None)),
                ('schoolyear_to', models.PositiveSmallIntegerField(default=None)),
                ('highschool', models.ForeignKey(default=None, to='mariners_profile.HighSchools')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
