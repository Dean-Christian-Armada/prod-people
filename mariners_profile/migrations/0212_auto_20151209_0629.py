# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0211_personaldata_availability_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='availability_date',
            field=models.DateField(default=None),
        ),
    ]
