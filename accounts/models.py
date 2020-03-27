from django.db import models


# Create your models here.
class User(models.Model):
    """用户的基础信息"""
    user_name = models.CharField("用户登录时的账户", max_length=64, unique=True)
    password = models.CharField("密码", max_length=255)

    class Meta:
        db_table = 'accounts_user'
