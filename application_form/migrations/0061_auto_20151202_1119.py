# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0060_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.ForeignKey(default=None, to='mariners_profile.Status'),
        ),
    ]
