# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20151113_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_url', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
