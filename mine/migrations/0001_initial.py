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
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=32, verbose_name='订单id')),
                ('goods_id', models.CharField(max_length=256, verbose_name='商品id')),
                ('goods_num', models.IntegerField(verbose_name='商品数量')),
            ],
            options={
                'db_table': 'mine_cart',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(verbose_name='订单唯一ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('status', models.SmallIntegerField(choices=[(10, '购物车'), (11, '已经生成订单'), (12, '已经付款'), (13, '已经发货'), (14, '已经收货'), (15, '已经删除')], default=11, verbose_name='订单状态')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
            ],
            options={
                'db_table': 'mine_order',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('order_id', 'goods_id')]),
        ),
    ]
