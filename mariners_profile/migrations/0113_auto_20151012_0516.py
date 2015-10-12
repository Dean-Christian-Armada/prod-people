# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0112_trainingcertificatedocumentsdetailed_training_place_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='src',
            name='src_rank',
            field=models.ForeignKey(default=b"mariners_profile.null_default_foreign_key_value(Rank, 'rank', '')", to='mariners_profile.Rank'),
        ),
    ]
