# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0005_auto_20150906_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='age',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='availability_date',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='birth_place',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='civil_status',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='email_address_1',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='email_address_2',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='landline_1',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='landline_2',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='mobile_1',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='mobile_2',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='pagibig',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='philhealth',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='preferred_vessel_type',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='sss',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='tin',
        ),
    ]
