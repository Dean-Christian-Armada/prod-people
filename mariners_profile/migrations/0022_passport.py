# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0021_auto_20150908_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None)),
                ('place_issued', models.ForeignKey(default=None, blank=True, to='mariners_profile.PassportPlaceIssued')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
