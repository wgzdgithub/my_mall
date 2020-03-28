from django.db import models

# Create your models here.
from accounts.models import User
from mall.models import Product

ORDER_STATUS_INIT = 10
ORDER_STATUS_SUBMIT = 11
ORDER_STATUS_PAIED = 12
ORDER_STATUS_SENT = 13
ORDER_STATUS_DONE = 14
ORDER_STATUS_DELETED = 15
ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_INIT, '购物车'),
    (ORDER_STATUS_SUBMIT, '已经生成订单'),
    (ORDER_STATUS_PAIED, '已经付款'),
    (ORDER_STATUS_SENT, '已经发货'),
    (ORDER_STATUS_DONE, '已经收货'),
    (ORDER_STATUS_DELETED, '已经删除'),
)


class Order(models.Model):
    """订单模块"""
    order_id = models.CharField("订单唯一ID", max_length=32)
    user_id = models.ForeignKey(User, related_name='orders')
    address = models.CharField("收货地址", max_length=256)
    total_price = models.IntegerField("总价")
    status = models.SmallIntegerField("订单状态",
                                      choices=ORDER_STATUS_CHOICES,
                                      default=ORDER_STATUS_SUBMIT)
    goods_count = models.IntegerField("商品数量")

    class Meta:
        db_table = 'mine_order'


class Cart(models.Model):
    user_id = models.ForeignKey(User, related_name='carts')
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order, verbose_name='订单', null=True)
    count = models.PositiveIntegerField("购买数量")
    amount = models.FloatField('总额')
    create_time = models.DateTimeField("下单时间", auto_now_add=True)
    update_time = models.DateTimeField("购买日期", auto_now=True)
    status = models.SmallIntegerField('状态',
                                      choices=ORDER_STATUS_CHOICES,
                                      default=ORDER_STATUS_INIT)

    class Meta:
        db_table = 'mine_cart'
        unique_together = ("user_id", "product", "order")
