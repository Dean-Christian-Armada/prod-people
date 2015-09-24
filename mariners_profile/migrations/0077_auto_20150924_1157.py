# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0076_auto_20150924_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluations', models.TextField(default=None, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evalutation',
            field=models.ForeignKey(default=None, to='mariners_profile.Evaluations'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
