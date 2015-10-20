# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0138_auto_20151016_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propulsion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('propulsion', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('company_standard', models.NullBooleanField()),
            ],
        ),
    ]
