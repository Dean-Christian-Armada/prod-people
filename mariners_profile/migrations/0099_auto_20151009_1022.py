# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0098_auto_20151009_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandEmployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer_first_name', models.CharField(default=None, max_length=50, null=True)),
                ('employer_middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('employer_last_name', models.CharField(default=None, max_length=50, null=True)),
                ('start_date', models.DateField(default=None, null=True, blank=True)),
                ('end_date', models.DateField(default=None, null=True, blank=True)),
                ('contact_first_name', models.CharField(default=None, max_length=50, null=True)),
                ('contact_middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('contact_last_name', models.CharField(default=None, max_length=50, null=True)),
                ('contact_person_number', models.BigIntegerField(default=None, null=True, blank=True)),
                ('employer_street', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('employer_unit', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('employer_zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
            ],
        ),
        migrations.CreateModel(
            name='LandPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('land_position', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='landemployment',
            name='position',
            field=models.ForeignKey(default=None, to='mariners_profile.LandPosition'),
        ),
        migrations.AddField(
            model_name='landemployment',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
