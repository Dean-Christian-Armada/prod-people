# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0063_auto_20151208_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='availability_date',
            field=models.DateField(default=None),
        ),
    ]
