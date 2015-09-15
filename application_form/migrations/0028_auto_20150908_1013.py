# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0027_auto_20150908_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformschengenvisa',
            name='schengen_visa_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformusvisa',
            name='us_visa_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
