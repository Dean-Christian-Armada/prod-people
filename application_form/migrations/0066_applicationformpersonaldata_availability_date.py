# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0065_remove_applicationformpersonaldata_availability_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='availability_date',
            field=models.DateField(default=datetime.date(2015, 12, 9)),
        ),
    ]
