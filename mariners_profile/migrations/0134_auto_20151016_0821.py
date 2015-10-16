# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0133_auto_20151016_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='flags',
            name='principal_standard',
            field=models.ManyToManyField(to='mariners_profile.Principal', blank=True),
        ),
        migrations.AddField(
            model_name='trainingcertificates',
            name='principal_standard',
            field=models.ManyToManyField(to='mariners_profile.Principal', blank=True),
        ),
    ]
