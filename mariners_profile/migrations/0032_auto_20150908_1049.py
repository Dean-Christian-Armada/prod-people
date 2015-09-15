# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0031_auto_20150908_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlagDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlagDocumentsDetailed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sbook_number', models.PositiveIntegerField(blank=True)),
                ('sbook_expiry', models.DateField(null=True, blank=True)),
                ('license_number', models.PositiveIntegerField(blank=True)),
                ('license_expiry', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flags', models.CharField(default=None, max_length=50)),
                ('company_standard', models.NullBooleanField(default=False, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='flagdocumentsdetailed',
            name='flags',
            field=models.ForeignKey(to='mariners_profile.Flags'),
        ),
        migrations.AddField(
            model_name='flagdocumentsdetailed',
            name='flags_documents',
            field=models.ForeignKey(to='mariners_profile.FlagDocuments'),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='flags',
            field=models.ManyToManyField(default=None, to='mariners_profile.Flags', through='mariners_profile.FlagDocumentsDetailed', blank=True),
        ),
        migrations.AddField(
            model_name='flagdocuments',
            name='user',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
    ]
