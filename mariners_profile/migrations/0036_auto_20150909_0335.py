# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0035_chargedoffense_termination'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training_center', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificateDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrainingCertificateDocumentsDetailed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField()),
                ('issued', models.DateField()),
                ('place_trained', models.OneToOneField(to='mariners_profile.TrainingCenter')),
                ('trainings_certificate_documents', models.ForeignKey(to='mariners_profile.TrainingCertificateDocuments')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCertificates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trainings_certificates', models.CharField(default=None, max_length=100)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='trainingcertificatedocumentsdetailed',
            name='trainings_certificates',
            field=models.ForeignKey(to='mariners_profile.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='trainingcertificatedocuments',
            name='trainings_certificates',
            field=models.ManyToManyField(default=None, to='mariners_profile.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='trainingcertificatedocuments',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
