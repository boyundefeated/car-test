# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-07 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, default='', max_length=255, unique=True),
        ),
    ]
