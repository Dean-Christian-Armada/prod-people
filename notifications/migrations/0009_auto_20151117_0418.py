# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_emailnotification_greetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailnotification',
            name='greetings',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='emailnotification',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
