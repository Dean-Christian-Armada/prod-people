# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0056_departments'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='department',
            field=models.ForeignKey(default=6, to='mariners_profile.Departments'),
        ),
    ]
