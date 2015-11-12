# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20151112_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification', models.ForeignKey(to='notifications.Notification')),
                ('received', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=None, max_length=100)),
                ('label', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotificationReceivers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receiver', models.ManyToManyField(to='notifications.Notification')),
                ('status', models.ForeignKey(to='notifications.NotificationStatus')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.ForeignKey(to='notifications.NotificationStatus'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='emailnotification',
            name='notification_status',
            field=models.ForeignKey(to='notifications.NotificationStatus'),
        ),
    ]
