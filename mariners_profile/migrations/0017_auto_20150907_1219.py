# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0016_auto_20150907_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schoolyear_from', models.PositiveSmallIntegerField(default=None)),
                ('schoolyear_to', models.PositiveSmallIntegerField(default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='highschools',
            old_name='highschool',
            new_name='highschool_name',
        ),
        migrations.AddField(
            model_name='highschool',
            name='highschool',
            field=models.ForeignKey(default=None, to='mariners_profile.HighSchools'),
        ),
        migrations.AddField(
            model_name='highschool',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
