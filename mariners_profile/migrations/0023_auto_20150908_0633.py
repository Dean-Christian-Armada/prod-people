# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0022_passport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passport',
            old_name='expiry',
            new_name='passport_expiry',
        ),
        migrations.AlterField(
            model_name='passportplaceissued',
            name='place',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='sbookplaceissued',
            name='place',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
    ]
