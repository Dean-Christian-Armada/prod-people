# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0007_auto_20150906_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.PositiveIntegerField(default=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('barangay', models.ForeignKey(default=None, to='mariners_profile.Barangay')),
                ('municipality', models.ForeignKey(default=None, to='mariners_profile.Municipality')),
            ],
        ),
        migrations.AddField(
            model_name='permanentaddress',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='currentaddress',
            name='zip',
            field=models.ForeignKey(default=None, to='mariners_profile.Zip'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='current_address',
            field=models.ForeignKey(default=None, to='mariners_profile.CurrentAddress'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='permanent_address',
            field=models.ForeignKey(default=None, to='mariners_profile.PermanentAddress'),
        ),
    ]
