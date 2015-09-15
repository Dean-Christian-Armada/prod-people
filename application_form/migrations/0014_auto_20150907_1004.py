# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0013_auto_20150907_0856'),
        ('application_form', '0013_auto_20150907_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormCollege',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collegeyear_from', models.PositiveSmallIntegerField(default=None)),
                ('collegeyear_to', models.PositiveSmallIntegerField(default=None)),
                ('college', models.ForeignKey(default=None, to='mariners_profile.Colleges')),
                ('degree', models.ForeignKey(default=None, to='mariners_profile.Degree')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='mother_name',
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='father_first_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='father_last_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='father_middle_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mother_first_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mother_last_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mother_middle_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
