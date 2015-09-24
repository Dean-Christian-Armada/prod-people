# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0042_auto_20150915_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcoc',
            name='coc',
            field=models.CharField(default=None, max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformcoc',
            name='coc_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformgoc',
            name='goc',
            field=models.CharField(default=None, max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformgoc',
            name='goc_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
