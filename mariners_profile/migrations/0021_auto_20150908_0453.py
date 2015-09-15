# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0020_auto_20150908_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplinaryaction',
            old_name='disciplinary_reason',
            new_name='disciplinary_action_reason',
        ),
        migrations.RenameField(
            model_name='visaapplication',
            old_name='visa_reason',
            new_name='visa_application_reason',
        ),
    ]
