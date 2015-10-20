# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0143_yellowfever_yellow_fever_issuing_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='english',
            field=models.ForeignKey(default=5, to='mariners_profile.English'),
        ),
        migrations.AlterField(
            model_name='primaryschool',
            name='primaryschool',
            field=models.ForeignKey(default=4, blank=True, to='mariners_profile.PrimarySchools', null=True),
        ),
        migrations.AlterField(
            model_name='vocational',
            name='vocational',
            field=models.ForeignKey(default=3, blank=True, to='mariners_profile.Vocationals', null=True),
        ),
    ]
