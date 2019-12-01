# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-19 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190411_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_b', models.CharField(max_length=100, unique_for_date='posted_b', verbose_name='Заголовок')),
                ('description_b', models.TextField(verbose_name='Краткое содержание')),
                ('content_b', models.TextField(verbose_name='Полное содержание')),
                ('posted_b', models.DateTimeField(db_index=True, default=datetime.datetime(2019, 5, 19, 23, 50, 0, 818637), verbose_name='Опубликована')),
                ('image_b', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке')),
                ('kol', models.IntegerField(default=1, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Копия статья блога',
                'verbose_name_plural': 'Копиистатьи блога',
                'db_table': 'Baskets',
                'ordering': ['-posted_b'],
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 5, 19, 23, 50, 0, 817637), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 5, 19, 23, 50, 0, 817637), verbose_name='Дата'),
        ),
    ]