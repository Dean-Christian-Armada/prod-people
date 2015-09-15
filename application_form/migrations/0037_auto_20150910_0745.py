# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0043_remove_seaservice_date_modified'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0036_remove_applicationformseaservice_date_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=None, upload_to=b'photos/application-form', blank=True)),
                ('signatures', models.ImageField(default=None, upload_to=b'signatures/application-form', blank=True)),
                ('application_date', models.DateField(default=None)),
                ('essay', models.TextField(default=None, null=True, blank=True)),
                ('alternative_position', models.ForeignKey(related_name='alternative_position', default=None, to='mariners_profile.Rank')),
            ],
        ),
        migrations.CreateModel(
            name='AppSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(default=None, to='mariners_profile.Sources')),
                ('specific', models.ForeignKey(default=None, to='mariners_profile.Specifics')),
            ],
        ),
        migrations.AddField(
            model_name='applicationform',
            name='application_source',
            field=models.ForeignKey(default=None, to='application_form.AppSource'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='position_applied',
            field=models.ForeignKey(related_name='position_applied', default=None, to='mariners_profile.Rank'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='status',
            field=models.ForeignKey(default=None, to='mariners_profile.Status'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='user',
            field=models.ForeignKey(default=None, to='login.UserProfile'),
        ),
    ]
