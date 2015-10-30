# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0171_marinersprofile_status_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinersprofile',
            name='picture_last_modified',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marinersprofile',
            name='status_last_modified',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
