# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0128_auto_20151014_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='since',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='until',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
