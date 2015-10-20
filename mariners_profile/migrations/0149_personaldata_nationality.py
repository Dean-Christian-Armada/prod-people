# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0148_auto_20151019_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='nationality',
            field=models.ForeignKey(default=1, to='mariners_profile.Nationality'),
        ),
    ]
