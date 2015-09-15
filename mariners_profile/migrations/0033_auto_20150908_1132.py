# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0032_auto_20150908_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flagdocuments',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
