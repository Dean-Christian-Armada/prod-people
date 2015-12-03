# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0061_auto_20151202_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.ForeignKey(default=3, to='mariners_profile.Status'),
        ),
    ]
