# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0041_auto_20150915_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformlicense',
            name='license',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
