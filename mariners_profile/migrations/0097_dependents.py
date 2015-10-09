# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0096_auto_20151008_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dependent_first_name', models.CharField(default=None, max_length=50, null=True)),
                ('dependent_middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('dependent_last_name', models.CharField(default=None, max_length=50, null=True)),
                ('dependent_contact', models.BigIntegerField(default=None, null=True, blank=True)),
                ('dependent_street', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('dependent_unit', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('dependent_relationship', models.ForeignKey(default=None, to='mariners_profile.Relationship')),
                ('dependent_zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
    ]
