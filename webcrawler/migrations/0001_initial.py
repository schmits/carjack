# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('model', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('license', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(to='webcrawler.Brand')),
            ],
        ),
    ]
