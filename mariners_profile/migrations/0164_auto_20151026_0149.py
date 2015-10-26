# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0163_delete_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='principal_code',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_principal',
            field=models.ForeignKey(default=0, to='mariners_profile.Principal'),
        ),
    ]
