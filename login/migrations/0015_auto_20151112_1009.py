# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20151101_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 10, 9, 19, 812532, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 10, 9, 25, 252506, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
