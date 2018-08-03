# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-03 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180803_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='blog.User'),
        ),
    ]
