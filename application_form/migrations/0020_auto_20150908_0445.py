# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0019_applicationformdetained_applicationformdisciplinaryaction_applicationformvisaapplication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationformdetained',
            old_name='reason',
            new_name='detained_reason',
        ),
        migrations.RenameField(
            model_name='applicationformdisciplinaryaction',
            old_name='reason',
            new_name='disciplinary_reason',
        ),
        migrations.RenameField(
            model_name='applicationformvisaapplication',
            old_name='reason',
            new_name='visa_reason',
        ),
    ]
