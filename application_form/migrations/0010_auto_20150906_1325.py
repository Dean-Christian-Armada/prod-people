# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0009_auto_20150906_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationformcurrentaddress',
            old_name='street',
            new_name='current_street',
        ),
        migrations.RenameField(
            model_name='applicationformcurrentaddress',
            old_name='unit',
            new_name='current_unit',
        ),
        migrations.RenameField(
            model_name='applicationformcurrentaddress',
            old_name='zip',
            new_name='current_zip',
        ),
        migrations.RenameField(
            model_name='applicationformpermanentaddress',
            old_name='street',
            new_name='permanent_street',
        ),
        migrations.RenameField(
            model_name='applicationformpermanentaddress',
            old_name='unit',
            new_name='permanent_unit',
        ),
        migrations.RenameField(
            model_name='applicationformpermanentaddress',
            old_name='zip',
            new_name='permanent_zip',
        ),
    ]
