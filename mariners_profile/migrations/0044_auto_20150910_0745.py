# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0043_remove_seaservice_date_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinersProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.NullBooleanField(default=0)),
                ('picture', models.ImageField(default=None, upload_to=b'photos/mariners-profile', blank=True)),
                ('signatures', models.ImageField(default=None, upload_to=b'signatures/mariners-profile', blank=True)),
                ('position', models.ForeignKey(to='mariners_profile.Rank')),
            ],
        ),
        migrations.CreateModel(
            name='ReferrersPool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, max_length=30)),
                ('middle_name', models.CharField(default=None, max_length=30, blank=True)),
                ('last_name', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='marinersprofile',
            name='referrer',
            field=models.ForeignKey(to='mariners_profile.ReferrersPool'),
        ),
        migrations.AddField(
            model_name='marinersprofile',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
