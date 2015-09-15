# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0037_auto_20150910_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('essay', models.TextField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='essay',
            field=models.ForeignKey(default=None, to='application_form.Essay'),
        ),
    ]
