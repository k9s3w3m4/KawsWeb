# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KawsWebEnter', '0002_auto_20170303_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPlanVersion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('targetversion', models.FloatField(blank=True, max_length=20)),
                ('versionplan', models.CharField(blank=True, max_length=4000, null=True)),
                ('creattime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
