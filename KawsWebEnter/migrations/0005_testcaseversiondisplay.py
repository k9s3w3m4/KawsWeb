# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KawsWebEnter', '0004_testplatformintroduce'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseVersionDisplay',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('versionname', models.CharField(blank=True, max_length=30, null=True)),
                ('versionintroduce', models.CharField(blank=True, max_length=255, null=True)),
                ('testlinkurl', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
