# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0007_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
