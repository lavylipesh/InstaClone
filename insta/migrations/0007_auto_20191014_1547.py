# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-14 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_auto_20191014_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
