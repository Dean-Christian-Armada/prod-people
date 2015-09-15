# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0044_auto_20150910_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='hiring',
            field=models.BooleanField(default=0),
        ),
    ]
