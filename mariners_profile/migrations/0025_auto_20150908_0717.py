# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0024_auto_20150908_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='COCRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coc_rank', models.CharField(default=None, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='coc',
            name='rank',
            field=models.ForeignKey(default=None, to='mariners_profile.COCRank'),
        ),
        migrations.AlterField(
            model_name='license',
            name='license',
            field=models.CharField(default=None, unique=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_expiry',
            field=models.DateField(default=None, blank=True),
        ),
    ]
