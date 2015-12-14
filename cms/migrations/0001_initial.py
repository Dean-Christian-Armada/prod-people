# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20151101_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50)),
                ('type', models.CharField(default='text', max_length=10)),
                ('classes', models.CharField(default='form-control input-form', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.FileField(upload_to=cms.models.content_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='FileFieldValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(default=None, max_length=50)),
                ('field', models.ForeignKey(to='cms.Fields')),
                ('file', models.ForeignKey(to='cms.File')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubFolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100)),
                ('folder', models.ForeignKey(to='cms.Folder')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='location',
            field=models.ForeignKey(to='cms.SubFolder'),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='fields',
            name='location',
            field=models.ForeignKey(to='cms.SubFolder'),
        ),
    ]
