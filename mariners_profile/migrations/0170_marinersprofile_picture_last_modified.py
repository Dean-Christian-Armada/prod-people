# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0169_auto_20151029_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinersprofile',
            name='picture_last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 29, 12, 46, 27, 605888, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
