# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notificationhistory_boolean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotificationreceivers',
            name='receiver',
            field=models.ManyToManyField(to='login.UserProfile'),
        ),
    ]
