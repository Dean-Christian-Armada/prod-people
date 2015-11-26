# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0058_applicationformspouse_spouse_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='hp',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformseaservice',
            name='kw',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=1, blank=True),
        ),
    ]
