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
    order_id = models.IntegerField("订单唯一ID")
    user_id = models.IntegerField('用户ID')
    status = models.SmallIntegerField("订单状态",
                                      choices=ORDER_STATUS_CHOICES,
                                      default=ORDER_STATUS_SUBMIT)
    order_time = models.DateTimeField("下单时间", auto_now_add=True)

    class Meta:
        db_table = 'mine_order'


class Cart(models.Model):
    order_id = models.CharField('订单id', max_length=32)
    goods_id = models.CharField('商品id', max_length=256)

    class Meta:
        db_table = 'mine_cart'
        unique_together = ("order_id", "goods_id")
