# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0170_marinersprofile_picture_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinersprofile',
            name='status_last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 29, 13, 13, 9, 251165, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
