# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0053_auto_20151026_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='availability_date',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
