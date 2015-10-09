# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0086_auto_20151002_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrincipalVesselType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('principal', models.ForeignKey(to='mariners_profile.Principal')),
                ('vessel_type', models.ManyToManyField(to='mariners_profile.VesselType')),
            ],
        ),
    ]
