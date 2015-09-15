# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0026_auto_20150908_0726'),
        ('application_form', '0025_auto_20150908_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationformcoc',
            old_name='rank',
            new_name='coc_rank',
        ),
        migrations.RemoveField(
            model_name='applicationformlicense',
            name='license_expiry',
        ),
        migrations.AddField(
            model_name='applicationformlicense',
            name='license_rank',
            field=models.ForeignKey(default=None, to='mariners_profile.Rank'),
        ),
    ]
