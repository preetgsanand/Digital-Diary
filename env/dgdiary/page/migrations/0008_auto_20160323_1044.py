# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20160320_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
