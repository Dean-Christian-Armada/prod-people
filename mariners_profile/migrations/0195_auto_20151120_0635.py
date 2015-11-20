# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0194_auto_20151119_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barangay',
            options={'ordering': ['barangay']},
        ),
        migrations.AlterModelOptions(
            name='dialect',
            options={'ordering': ['dialect']},
        ),
        migrations.AddField(
            model_name='dependents',
            name='dependent_birth_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
