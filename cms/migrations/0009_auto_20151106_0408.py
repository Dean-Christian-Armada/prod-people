# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_subfolder_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploaded_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
