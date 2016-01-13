# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0216_marinersprofilepicturelog_marinersprofilestatuslog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marinersprofilestatuslog',
            name='mariners_profile',
        ),
        migrations.RemoveField(
            model_name='marinersprofilestatuslog',
            name='user',
        ),
        migrations.DeleteModel(
            name='MarinersProfileStatusLog',
        ),
    ]
