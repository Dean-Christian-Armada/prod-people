# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0217_auto_20160112_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evaluated_by',
            field=models.ForeignKey(to='login.UserProfile', default=None, related_name='evaluated_by'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='updated_by',
            field=models.ForeignKey(to='login.UserProfile', default=None, related_name='updated_by'),
        ),
    ]
