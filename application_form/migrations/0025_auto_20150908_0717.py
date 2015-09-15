# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0024_applicationformcoc_applicationformgoc_applicationformlicense_applicationformsbook_applicationformsch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcoc',
            name='rank',
            field=models.ForeignKey(default=None, to='mariners_profile.COCRank'),
        ),
        migrations.AlterField(
            model_name='applicationformlicense',
            name='license',
            field=models.CharField(default=None, unique=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformlicense',
            name='license_expiry',
            field=models.DateField(default=None, blank=True),
        ),
    ]
