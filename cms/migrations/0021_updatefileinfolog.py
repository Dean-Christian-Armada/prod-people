# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_userprofile_departmental_email'),
        ('cms', '0020_auto_20160104_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateFileInfoLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.ForeignKey(to='cms.File')),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
    ]
