# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20151112_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='departmental_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
    ]
