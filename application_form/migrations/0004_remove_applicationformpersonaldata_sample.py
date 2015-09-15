# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0003_applicationformpersonaldata_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='sample',
        ),
    ]
