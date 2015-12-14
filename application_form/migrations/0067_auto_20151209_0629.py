# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0066_applicationformpersonaldata_availability_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='availability_date',
            field=models.DateField(default=None),
        ),
    ]
