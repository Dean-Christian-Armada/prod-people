# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0012_auto_20150907_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_1',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_2',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
    ]
