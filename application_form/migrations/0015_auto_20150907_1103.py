# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0014_auto_20150907_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformspouse',
            name='spouse_contact',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
    ]
