# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lambda', '0002_auto_20160924_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lambda.Profile'),
        ),
    ]
