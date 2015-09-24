# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0077_auto_20150924_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evalutation',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
