# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0136_auto_20151016_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principal',
            old_name='training_certificate_standard',
            new_name='trainings_certificate_standard',
        ),
    ]
