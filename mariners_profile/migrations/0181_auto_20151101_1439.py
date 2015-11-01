# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0180_auto_20151101_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evaluated_by',
            field=models.ForeignKey(related_name='evaluated_by', default=321, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by', default=321, to='login.UserProfile'),
        ),
    ]
