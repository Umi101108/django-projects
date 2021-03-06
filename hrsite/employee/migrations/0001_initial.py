# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'employee_information',
                'managed': False,
            },
        ),
    ]
