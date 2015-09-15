# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0036_auto_20150909_0335'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0031_applicationformchargedoffense_applicationformtermination'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormTrainingCertificateDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trainings_certificates', models.ManyToManyField(default=None, to='mariners_profile.TrainingCertificates')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
