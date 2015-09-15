# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0032_applicationformtrainingcertificatedocuments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcoc',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformemergencycontact',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformgoc',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformlicense',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformpassport',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='name',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformsbook',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformschengenvisa',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformspouse',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformsrc',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformusvisa',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='applicationformyellowfever',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
