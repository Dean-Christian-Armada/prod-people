# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0068_auto_20151211_0730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationformseaservice',
            options={'ordering': ['-date_left']},
        ),
    ]
