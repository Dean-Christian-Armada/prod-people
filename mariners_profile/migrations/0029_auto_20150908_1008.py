# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0028_auto_20150908_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='coc_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
