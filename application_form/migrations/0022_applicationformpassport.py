# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0021_auto_20150908_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormPassport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport', models.CharField(default=None, unique=True, max_length=100)),
                ('expiry', models.DateField(default=None)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
