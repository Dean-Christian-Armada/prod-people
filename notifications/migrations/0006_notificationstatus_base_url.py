# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_baseurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationstatus',
            name='base_url',
            field=models.ForeignKey(default=1, to='notifications.BaseURL'),
        ),
    ]
