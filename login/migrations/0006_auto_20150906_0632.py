# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20150906_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.CharField(blank=True, max_length=4, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^([a-z]{4})$', message=b'Please follow code format')]),
        ),
    ]
