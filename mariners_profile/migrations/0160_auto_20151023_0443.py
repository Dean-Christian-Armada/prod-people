# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0159_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='coc_place_issued',
            field=models.ForeignKey(default=5, blank=True, to='mariners_profile.COCPlaceIssued'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='availability_date',
            field=django_date_extensions.fields.ApproximateDateField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='instagram_email',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='twitter_email',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
    ]
