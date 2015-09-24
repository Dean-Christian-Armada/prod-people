# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0065_primaryschools'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimarySchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primaryschoolyear_from', models.PositiveSmallIntegerField(default=None)),
                ('primaryschoolyear_to', models.PositiveSmallIntegerField(default=None)),
                ('primaryschool', models.ForeignKey(default=None, to='mariners_profile.PrimarySchools')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Vocational',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocationalyear_from', models.PositiveSmallIntegerField(default=None)),
                ('vocationalyear_to', models.PositiveSmallIntegerField(default=None)),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
                ('vocational', models.ForeignKey(default=None, to='mariners_profile.Vocationals')),
            ],
        ),
    ]
