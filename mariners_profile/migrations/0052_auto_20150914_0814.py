# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0051_auto_20150911_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangay',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='cocrank',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='colleges',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='degree',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='enginetype',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='manningagency',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='municipality',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='passportplaceissued',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='rank',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='relationship',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='sbookplaceissued',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='vesseltype',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
    ]
