# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0165_auto_20151026_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldata',
            old_name='instagram_email',
            new_name='facebook_account',
        ),
        migrations.RenameField(
            model_name='personaldata',
            old_name='twitter_email',
            new_name='instagram_account',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='facebook_email',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='twitter_account',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='evaluated_by',
            field=models.ForeignKey(related_name='evaluated_by', default=321, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by', default=321, to='login.UserProfile'),
        ),
    ]
