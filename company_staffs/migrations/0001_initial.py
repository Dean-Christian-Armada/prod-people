# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20151112_1009'),
        ('mariners_profile', '0192_auto_20151112_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPositions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positions', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserCompanyProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('unit', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('contact', models.BigIntegerField(default=None, null=True, blank=True)),
                ('position', models.ForeignKey(to='company_staffs.CompanyPositions')),
                ('user', models.ForeignKey(to='login.UserProfile')),
                ('zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
            ],
        ),
    ]
