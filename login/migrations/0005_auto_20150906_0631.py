# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150906_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlevel',
            name='userlevel',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.CharField(max_length=4, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^([a-z]{4})$', message=b'Please follow code format')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
