# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0132_trainingcertificates_trainings_certificates_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinerstatushistory',
            name='updated_on',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 5, 12, 36, 447627, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='user',
            field=models.ForeignKey(related_name='mariner_user', default=None, to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='trainingcertificatedocumentsdetailed',
            name='place_trained',
            field=models.ForeignKey(default=1, to='mariners_profile.TrainingCenter'),
        ),
    ]
