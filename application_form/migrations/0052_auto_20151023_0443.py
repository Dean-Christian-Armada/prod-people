# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0051_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='availability_date',
            field=django_date_extensions.fields.ApproximateDateField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='instagram_email',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationformpersonaldata',
            name='twitter_email',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
        ),
    ]
