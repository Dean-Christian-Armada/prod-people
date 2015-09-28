# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0080_auto_20150928_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='health_problem',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
