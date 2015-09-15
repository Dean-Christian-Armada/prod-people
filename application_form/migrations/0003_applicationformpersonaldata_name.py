# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0002_auto_20150906_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='name',
            field=models.OneToOneField(default=None, to='login.UserProfile'),
        ),
    ]
