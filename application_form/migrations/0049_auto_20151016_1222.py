# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0048_auto_20151012_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='age',
        ),
        migrations.RemoveField(
            model_name='applicationformseaservice',
            name='duration',
        ),
    ]
