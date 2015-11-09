# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0055_applicationformpersonaldata_mobile_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='google_plus_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='linkedin_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='pinterest_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='reddit_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='tumblr_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
    ]
