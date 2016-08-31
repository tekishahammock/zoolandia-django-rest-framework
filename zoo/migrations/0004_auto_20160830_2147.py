# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_auto_20160830_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='habitat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo.Habitat'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='habitat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo.Habitat'),
        ),
    ]