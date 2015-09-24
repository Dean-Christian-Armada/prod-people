# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0044_auto_20150923_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcoc',
            name='coc',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformgoc',
            name='goc',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
