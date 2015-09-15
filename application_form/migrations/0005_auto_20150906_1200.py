# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0004_remove_applicationformpersonaldata_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='age',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='availability_date',
            field=django_date_extensions.fields.ApproximateDateField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='birth_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='email_address_1',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='email_address_2',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='father_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='landline_1',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='landline_2',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mobile_1',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mobile_2',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='mother_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='pagibig',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='philhealth',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='sss',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='tin',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
    ]
