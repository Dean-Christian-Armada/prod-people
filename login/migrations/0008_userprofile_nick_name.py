# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
