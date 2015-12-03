# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0206_auto_20151202_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='action',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='status',
            name='list_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='status',
            name='listed',
            field=models.BooleanField(default=False),
        ),
    ]
