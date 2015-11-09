# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0187_auto_20151105_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='google_plus_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='linkedin_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='pinterest_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='reddit_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='tumblr_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
    ]
