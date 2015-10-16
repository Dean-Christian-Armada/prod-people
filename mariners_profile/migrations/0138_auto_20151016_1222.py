# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0137_auto_20151016_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='age',
        ),
        migrations.RemoveField(
            model_name='seaservice',
            name='duration',
        ),
    ]
