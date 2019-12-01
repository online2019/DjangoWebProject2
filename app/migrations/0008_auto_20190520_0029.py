# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-19 21:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190519_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='content_b',
            field=models.TextField(default='Полное', verbose_name='Полное содержание'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='description_b',
            field=models.TextField(default='Краткое', verbose_name='Краткое содержание'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='posted_b',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 5, 20, 0, 29, 23, 57955), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='title_b',
            field=models.CharField(default='Заголовок', max_length=100, unique_for_date='posted_b', verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 5, 20, 0, 29, 23, 56955), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 5, 20, 0, 29, 23, 57955), verbose_name='Дата'),
        ),
    ]