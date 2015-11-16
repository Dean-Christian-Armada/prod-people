# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_notificationstatus_base_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationstatus',
            name='base_url',
            field=models.ForeignKey(default=None, to='notifications.BaseURL'),
        ),
    ]
