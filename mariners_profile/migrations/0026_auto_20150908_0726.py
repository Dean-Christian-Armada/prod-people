# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0025_auto_20150908_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coc',
            old_name='rank',
            new_name='coc_rank',
        ),
        migrations.AddField(
            model_name='license',
            name='license_rank',
            field=models.ForeignKey(default=None, to='mariners_profile.Rank'),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_date_issued',
            field=models.DateField(default=None, blank=True),
        ),
    ]
