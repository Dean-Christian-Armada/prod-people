# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0035_auto_20150909_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformseaservice',
            name='date_modified',
        ),
    ]
