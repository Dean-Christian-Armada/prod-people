# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0052_auto_20151023_0443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationformpersonaldata',
            old_name='instagram_email',
            new_name='facebook_account',
        ),
        migrations.RenameField(
            model_name='applicationformpersonaldata',
            old_name='twitter_email',
            new_name='instagram_account',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='facebook_email',
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='twitter_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
    ]
