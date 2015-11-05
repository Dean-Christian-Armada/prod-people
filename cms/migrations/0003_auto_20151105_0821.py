# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20151105_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(related_name='uploaded_by', default=None, to='login.UserProfile'),
        ),
    ]
