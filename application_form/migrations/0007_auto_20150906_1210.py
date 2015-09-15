# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0006_auto_20150906_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='age',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='availability_date',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='birth_place',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='civil_status',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='email_address_1',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='email_address_2',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='landline_1',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='landline_2',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='mobile_1',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='mobile_2',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='pagibig',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='philhealth',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='preferred_vessel_type',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='sss',
        ),
        migrations.RemoveField(
            model_name='applicationformpersonaldata',
            name='tin',
        ),
    ]
