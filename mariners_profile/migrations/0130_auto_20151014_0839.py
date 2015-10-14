# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0129_auto_20151014_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinerstatuscomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 8, 39, 4, 984585, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marinerstatuscomment',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 8, 39, 19, 536421, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
