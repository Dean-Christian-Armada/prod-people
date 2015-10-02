# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0046_auto_20151001_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformemergencycontact',
            name='emergency_contact',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
    ]
