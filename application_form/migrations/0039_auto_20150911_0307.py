# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0038_auto_20150910_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationform',
            old_name='signatures',
            new_name='signature',
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.ForeignKey(default=3, to='mariners_profile.Status'),
        ),
    ]
