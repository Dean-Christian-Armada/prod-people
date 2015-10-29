# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0054_auto_20151026_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mobile_3',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
    ]
