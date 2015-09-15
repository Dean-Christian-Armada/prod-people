# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0052_auto_20150914_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocrank',
            name='company_standard',
            field=models.NullBooleanField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='rank',
            name='company_standard',
            field=models.NullBooleanField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='vesseltype',
            name='company_standard',
            field=models.NullBooleanField(default=False, max_length=50),
        ),
    ]
