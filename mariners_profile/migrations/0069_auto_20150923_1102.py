# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0068_auto_20150923_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocational',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='vocational',
            name='vocational',
            field=models.ForeignKey(default=None, to='mariners_profile.Vocationals'),
        ),
        migrations.AddField(
            model_name='vocational',
            name='vocationalyear_from',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vocational',
            name='vocationalyear_to',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vocationals',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 11, 2, 20, 200790, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocationals',
            name='full_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='vocationals',
            name='vocational_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
