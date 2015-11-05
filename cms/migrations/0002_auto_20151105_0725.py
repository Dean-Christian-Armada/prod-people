# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20151101_1518'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='order',
            field=models.SmallIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(related_name='uploaded_by', default=271, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='file',
            name='uploaded_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 5, 7, 25, 11, 241489, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='order',
            field=models.SmallIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='subfolder',
            name='order',
            field=models.SmallIntegerField(default=None, null=True, blank=True),
        ),
    ]
