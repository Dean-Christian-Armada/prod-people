# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0036_auto_20150909_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingcertificatedocumentsdetailed',
            name='issued',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trainingcertificatedocumentsdetailed',
            name='number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
