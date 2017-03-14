# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testuser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('adress', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'testuser',
            },
        ),
    ]