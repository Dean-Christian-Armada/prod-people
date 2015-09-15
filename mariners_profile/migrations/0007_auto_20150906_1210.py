# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0006_auto_20150906_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='age',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='availability_date',
            field=django_date_extensions.fields.ApproximateDateField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='birth_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='birth_place',
            field=models.ForeignKey(default=None, to='mariners_profile.BirthPlace'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='civil_status',
            field=models.ForeignKey(default=None, to='mariners_profile.CivilStatus'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='email_address_1',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='email_address_2',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='father_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='landline_1',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='landline_2',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='mobile_1',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='mobile_2',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='mother_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='pagibig',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='philhealth',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='preferred_vessel_type',
            field=models.ForeignKey(default=None, to='mariners_profile.VesselType'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='sss',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='tin',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
    ]
