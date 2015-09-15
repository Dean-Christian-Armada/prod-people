# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0039_auto_20150911_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='duration',
            field=models.PositiveSmallIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='grt',
            field=models.PositiveIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='hp',
            field=models.DecimalField(default=None, max_digits=10, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='kw',
            field=models.DecimalField(default=None, max_digits=10, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='year_built',
            field=models.PositiveSmallIntegerField(default=None, blank=True),
        ),
    ]
