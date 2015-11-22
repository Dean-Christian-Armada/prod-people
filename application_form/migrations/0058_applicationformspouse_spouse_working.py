# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0057_auto_20151109_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformspouse',
            name='spouse_working',
            field=models.NullBooleanField(default=None),
        ),
    ]
