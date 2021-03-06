# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 14:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_date', models.DateField()),
                ('activity_time', models.TimeField()),
                ('activity_comment', models.CharField(max_length=2000)),
                ('payed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatars/no-img.jpg', upload_to='avatars/')),
                ('salary', models.FloatField()),
                ('timezone', models.CharField(default='Asia/Tehran', max_length=50)),
                ('id_number', models.IntegerField(unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile'),
        ),
    ]
