# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0153_auto_20151021_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='evaluated_on',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 13, 21, 16, 433266, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
