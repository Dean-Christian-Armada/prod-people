# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0209_auto_20151208_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='availability_date',
        ),
    ]
