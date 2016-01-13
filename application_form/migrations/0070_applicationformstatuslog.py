# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_userprofile_departmental_email'),
        ('application_form', '0069_auto_20160104_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormStatusLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('old_status', models.CharField(null=True, max_length=75, blank=True)),
                ('new_status', models.CharField(null=True, max_length=75, blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('application_form', models.ForeignKey(to='application_form.ApplicationForm')),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
    ]
