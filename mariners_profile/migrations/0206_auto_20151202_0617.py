# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0205_auto_20151202_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evaluated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
