# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20160320_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='photo',
            field=models.FileField(upload_to=page.models.content_file_name),
        ),
    ]