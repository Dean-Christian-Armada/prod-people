# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0093_auto_20151007_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_area', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
        ),
    ]
