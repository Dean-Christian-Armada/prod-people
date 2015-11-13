# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20151113_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationhistory',
            name='notification',
            field=models.ForeignKey(blank=True, to='notifications.Notification', null=True),
        ),
        migrations.AlterField(
            model_name='notificationhistory',
            name='received',
            field=models.ForeignKey(blank=True, to='login.UserProfile', null=True),
        ),
    ]
