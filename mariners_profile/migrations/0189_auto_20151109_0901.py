# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0188_auto_20151109_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldata',
            old_name='google_plus_account',
            new_name='googleplus_account',
        ),
    ]
