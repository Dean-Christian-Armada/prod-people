# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0010_auto_20150907_0445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spouse_name', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('married_date', models.DateField(default=None, null=True, blank=True)),
                ('birthdate', models.DateField(default=None, null=True, blank=True)),
                ('spouse_contact', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
