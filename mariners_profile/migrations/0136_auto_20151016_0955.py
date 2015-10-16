# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0135_auto_20151016_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingcertificates',
            name='departments',
            field=models.ManyToManyField(to='mariners_profile.Departments', blank=True),
        ),
    ]
