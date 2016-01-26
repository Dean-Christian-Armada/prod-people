# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_userprofile_departmental_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlevel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 26, 8, 37, 56, 647308, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userlevel',
            field=models.ForeignKey(default=None, to='login.Userlevel'),
        ),
    ]
