# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0085_delete_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='emergency_contact',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
    ]
