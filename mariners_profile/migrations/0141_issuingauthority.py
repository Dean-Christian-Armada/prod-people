# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0140_auto_20151019_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuingAuthority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issuing_authority', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True)),
            ],
        ),
    ]
