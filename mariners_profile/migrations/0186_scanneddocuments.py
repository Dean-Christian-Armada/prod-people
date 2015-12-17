# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
# from globals_declarations.methods import content_file_name
import cms.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20151101_1518'),
        ('mariners_profile', '0185_dynamicpathfolders'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScannedDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scan', models.ImageField(upload_to=cms.models.content_file_name, blank=True)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('archive', models.BooleanField(default=False)),
                ('folder_path', models.ForeignKey(default=None, to='mariners_profile.DynamicPathFolders')),
                ('uploaded_by', models.ForeignKey(related_name='uploaded_by', default=321, to='login.UserProfile')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
            ],
        ),
    ]
