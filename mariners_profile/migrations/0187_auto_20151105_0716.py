# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0186_scanneddocuments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanneddocuments',
            name='folder_path',
        ),
        migrations.RemoveField(
            model_name='scanneddocuments',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='scanneddocuments',
            name='user',
        ),
        migrations.DeleteModel(
            name='DynamicPathFolders',
        ),
        migrations.DeleteModel(
            name='ScannedDocuments',
        ),
    ]
