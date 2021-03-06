# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-03-29 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, unique=True, verbose_name='用户登录时的账户')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
            ],
            options={
                'db_table': 'accounts_user',
            },
        ),
    ]
