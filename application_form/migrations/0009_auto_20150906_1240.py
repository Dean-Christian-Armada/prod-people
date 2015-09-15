# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0008_auto_20150906_1240'),
        ('application_form', '0008_auto_20150906_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormCurrentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50, null=True)),
                ('zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationFormPermanentAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(default=None, max_length=50)),
                ('street', models.CharField(default=None, max_length=50, null=True)),
                ('zip', models.ForeignKey(default=None, to='mariners_profile.Zip')),
            ],
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='current_address',
            field=models.ForeignKey(default=None, to='application_form.ApplicationFormCurrentAddress'),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='permanent_address',
            field=models.ForeignKey(default=None, to='application_form.ApplicationFormPermanentAddress'),
        ),
    ]
