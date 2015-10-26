# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0164_auto_20151026_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evaluated_by',
            field=models.ForeignKey(related_name='evaluated_by', default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_principal',
            field=models.ForeignKey(default=26, to='mariners_profile.Principal'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by', default=None, to='login.UserProfile'),
        ),
    ]
