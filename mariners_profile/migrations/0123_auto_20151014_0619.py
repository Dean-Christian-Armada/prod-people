# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0122_auto_20151013_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='flags',
            name='manship_standard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='principal',
            name='manship_standard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vesselname',
            name='manship_standard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='manship_standard',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='flags',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
    ]
