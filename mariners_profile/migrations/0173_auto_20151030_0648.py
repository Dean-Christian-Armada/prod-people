# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0172_auto_20151029_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='dialect',
            field=models.ForeignKey(default=46, to='mariners_profile.Dialect'),
        ),
    ]
