# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0049_auto_20151016_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='facebook_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='instagram_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='twitter_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
    ]
