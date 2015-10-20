# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0149_personaldata_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='facebook_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='instagram_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='twitter_email',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
    ]
