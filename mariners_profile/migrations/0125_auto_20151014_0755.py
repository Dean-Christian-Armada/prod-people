# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0124_auto_20151014_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mariner_status', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='marinersprofile',
            name='mariner_principal',
            field=models.ForeignKey(default=26, to='mariners_profile.Principal'),
        ),
    ]
