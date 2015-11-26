# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_userprofile_departmental_email'),
        ('mariners_profile', '0199_auto_20151123_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinerStatusHistoryAuthority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MarinerStatusHistoryPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MarinerStatusHistoryPermissionFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acknowledgement_file', models.FileField(upload_to=b'mariner-status-history-change-principal-files')),
                ('history', models.ForeignKey(to='mariners_profile.MarinerStatusHistory')),
            ],
        ),
        migrations.AddField(
            model_name='marinerstatushistorypermission',
            name='mariner_history_with_file',
            field=models.ForeignKey(to='mariners_profile.MarinerStatusHistoryPermissionFile'),
        ),
        migrations.AddField(
            model_name='marinerstatushistorypermission',
            name='user',
            field=models.ForeignKey(to='mariners_profile.MarinerStatusHistoryAuthority'),
        ),
    ]
