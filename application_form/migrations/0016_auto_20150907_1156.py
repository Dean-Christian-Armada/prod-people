# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0015_auto_20150907_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcollege',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
