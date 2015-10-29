# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0168_auto_20151028_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='mobile_3',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='employer_zip',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Zip'),
        ),
        migrations.AlterField(
            model_name='landemployment',
            name='land_position',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.LandPosition'),
        ),
    ]
