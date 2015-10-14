# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0127_auto_20151014_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinerStatusComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mariner_status_comment', models.TextField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='marinersprofile',
            name='mariner_principal',
        ),
        migrations.RemoveField(
            model_name='marinersprofile',
            name='mariner_status',
        ),
    ]
