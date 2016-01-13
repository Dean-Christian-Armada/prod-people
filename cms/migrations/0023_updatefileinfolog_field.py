# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20160111_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatefileinfolog',
            name='field',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
