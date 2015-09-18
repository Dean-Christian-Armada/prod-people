# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0060_auto_20150918_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingcertificates',
            name='departments',
            field=models.ManyToManyField(default=5, to='mariners_profile.Departments'),
        ),
    ]
