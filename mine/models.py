from django.db import models

# Create your models here.
from accounts.models import User
from mall.models import Product

ORDER_STATUS_SUBMIT = 11
ORDER_STATUS_PAIED = 12
ORDER_STATUS_SENT = 13
ORDER_STATUS_DONE = 14
ORDER_STATUS_DELETED = 15
ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_SUBMIT, '已经生成订单'),
    (ORDER_STATUS_PAIED, '已经付款'),
    (ORDER_STATUS_SENT, '已经发货'),
    (ORDER_STATUS_DONE, '已经收货'),
    (ORDER_STATUS_DELETED, '已经删除'),
)


class Order(models.Model):
    order_id = models.CharField("订单唯一ID", max_length=32)
    user_id = models.ForeignKey(User, related_name='orders')
    product = models.ForeignKey(Product)
    address = models.CharField("收货地址", max_length=256)
    create_time = models.DateTimeField("下单时间", auto_now_add=True)
    update_time = models.DateTimeField("购买日期", auto_now=True)
    total_price = models.IntegerField("总价")
    status = models.SmallIntegerField("订单状态",
                                      choices=ORDER_STATUS_CHOICES,
                                      default=ORDER_STATUS_SUBMIT)
    goods_count = models.IntegerField("商品数量")

    class Meta:
        db_table = 'mine_order'
