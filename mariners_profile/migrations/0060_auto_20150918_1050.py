# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0059_flags_departments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flags',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='trainingcertificates',
            name='department',
        ),
        migrations.AddField(
            model_name='trainingcertificates',
            name='departments',
            field=models.ManyToManyField(default=6, to='mariners_profile.Departments'),
        ),
    ]
