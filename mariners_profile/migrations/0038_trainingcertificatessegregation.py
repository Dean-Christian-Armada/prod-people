# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0037_auto_20150909_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingCertificatesSegregation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('segregation', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
