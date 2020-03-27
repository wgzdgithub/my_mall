# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-03-27 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=32, verbose_name='订单唯一ID')),
                ('address', models.CharField(max_length=256, verbose_name='收货地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='购买日期')),
                ('total_price', models.IntegerField(verbose_name='总价')),
                ('status', models.SmallIntegerField(choices=[(11, '已经生成订单'), (12, '已经付款'), (13, '已经发货'), (14, '已经收货'), (15, '已经删除')], default=11, verbose_name='订单状态')),
                ('goods_count', models.IntegerField(verbose_name='商品数量')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.User')),
            ],
            options={
                'db_table': 'mine_order',
            },
        ),
    ]
