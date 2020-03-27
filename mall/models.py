from django.db import models
import uuid

# Create your models here.
PRODUCT_TYPES_ACTUAL = 11
PRODUCT_TYPES_VIRTUAL = 12
PRODUCT_TYPES_CHOICES = (
    (PRODUCT_TYPES_ACTUAL, '实物商品'),
    (PRODUCT_TYPES_VIRTUAL, '虚拟商品')
)


class Product(models.Model):
    uid = models.UUIDField("商品唯一ID", default=uuid.uuid4(), editable=False)
    name = models.CharField("商品名字", max_length=128)
    price = models.IntegerField("商品价格")
    category = models.SmallIntegerField("商品种类",
                                        choices=PRODUCT_TYPES_CHOICES,
                                        default=PRODUCT_TYPES_ACTUAL)

    class Meta:
        db_table = 'mall_product'
