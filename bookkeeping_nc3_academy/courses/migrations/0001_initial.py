# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, null=True)),
                ('course', models.CharField(max_length=50)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('description', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]