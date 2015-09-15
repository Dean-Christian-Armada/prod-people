# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0019_detained_disciplinaryaction_visaapplication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detained',
            old_name='reason',
            new_name='detained_reason',
        ),
        migrations.RenameField(
            model_name='disciplinaryaction',
            old_name='reason',
            new_name='disciplinary_reason',
        ),
        migrations.RenameField(
            model_name='visaapplication',
            old_name='reason',
            new_name='visa_reason',
        ),
    ]
