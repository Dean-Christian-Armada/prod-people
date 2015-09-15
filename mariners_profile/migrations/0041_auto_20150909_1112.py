# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0040_auto_20150909_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='goc',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='license',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='name',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='sbook',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='schengenvisa',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='src',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='usvisa',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
