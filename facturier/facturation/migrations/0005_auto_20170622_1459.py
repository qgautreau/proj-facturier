# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturation', '0004_auto_20170622_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='mail',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mail',
            field=models.CharField(max_length=30, null=True),
        ),
    ]