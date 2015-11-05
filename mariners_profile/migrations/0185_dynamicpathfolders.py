# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0184_auto_20151103_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicPathFolders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
        ),
    ]
