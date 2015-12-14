# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0210_remove_personaldata_availability_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='availability_date',
            field=models.DateField(default=datetime.date(2015, 12, 9)),
        ),
    ]
