# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='siret',
            field=models.IntegerField(verbose_name='SIRET'),
        ),
    ]