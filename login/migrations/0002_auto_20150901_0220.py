# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phrase',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(regex=b'^([a-z]{4})$', message=b'Please follow code format')]),
        ),
    ]
