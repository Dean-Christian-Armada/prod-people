# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0125_auto_20151014_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinerStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('since', models.DateField(default=None)),
                ('until', models.DateField(default=None)),
                ('mariner_principal', models.ForeignKey(default=26, to='mariners_profile.Principal')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NonConformingSeafarerReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('non_conforming_reason', models.TextField(default=None)),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='marinerstatus',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
    ]
