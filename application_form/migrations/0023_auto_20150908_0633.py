# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0022_applicationformpassport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationformpassport',
            old_name='expiry',
            new_name='passport_expiry',
        ),
    ]
