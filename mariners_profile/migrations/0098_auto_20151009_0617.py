# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0097_dependents'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='dialect',
            field=models.ForeignKey(default=1, to='mariners_profile.Dialect'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='english',
            field=models.ForeignKey(default=1, to='mariners_profile.English'),
        ),
        migrations.AlterField(
            model_name='dialect',
            name='dialect',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='english',
            name='english',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
