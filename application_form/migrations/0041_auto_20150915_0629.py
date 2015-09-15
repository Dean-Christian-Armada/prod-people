# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0040_auto_20150911_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='grt',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
    ]
