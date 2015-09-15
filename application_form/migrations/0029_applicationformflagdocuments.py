# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0032_auto_20150908_1049'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0028_auto_20150908_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormFlagDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flags', models.ManyToManyField(default=None, to='mariners_profile.Flags', blank=True)),
                ('user', models.OneToOneField(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
