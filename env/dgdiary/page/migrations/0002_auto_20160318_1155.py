# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-18 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageModel',
            new_name='Page',
        ),
    ]
