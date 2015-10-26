# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0166_auto_20151026_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='availability_date',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
