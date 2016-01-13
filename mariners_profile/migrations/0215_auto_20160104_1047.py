# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0214_auto_20151211_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seaservice',
            options={'ordering': ['-date_left']},
        ),
    ]
