# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0114_remove_passport_passport_date_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntclicense',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='stcwcertificate',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='stcwendorsement',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
