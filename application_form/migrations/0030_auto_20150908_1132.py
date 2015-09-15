# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0029_applicationformflagdocuments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformflagdocuments',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
