# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20151116_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='greetings',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
