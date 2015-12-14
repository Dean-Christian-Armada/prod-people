# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0064_auto_20151208_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='availability_date',
        ),
    ]
