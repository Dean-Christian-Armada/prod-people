# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0017_auto_20150907_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emergency_first_name', models.CharField(default=None, max_length=50, null=True)),
                ('emergency_middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('emergency_last_name', models.CharField(default=None, max_length=50, null=True)),
                ('emergency_contact', models.CharField(default=None, max_length=100, null=True)),
                ('emergency_street', models.CharField(default=None, max_length=50, null=True)),
                ('emergency_unit', models.CharField(default=None, max_length=50, null=True)),
                ('emergency_zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
                ('relationship', models.ForeignKey(default=None, to='mariners_profile.Relationship')),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
