# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_userprofile_departmental_email'),
        ('mariners_profile', '0215_auto_20160104_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinersProfilePictureLog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('old_picture', models.ImageField(upload_to='', null=True, blank=True, max_length=75)),
                ('new_picture', models.ImageField(upload_to='', null=True, blank=True, max_length=75)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('mariners_profile', models.ForeignKey(to='mariners_profile.MarinersProfile')),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MarinersProfileStatusLog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('old_status', models.CharField(null=True, blank=True, max_length=75)),
                ('new_status', models.CharField(null=True, blank=True, max_length=75)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('mariners_profile', models.ForeignKey(to='mariners_profile.MarinersProfile')),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
    ]
