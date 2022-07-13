from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    #1, 增加额外的属性
    mobile = models.CharField(verbose_name="手机号",max_length=11,unique=True)

    #2,是否激活邮箱
    email_active = models.BooleanField(verbose_name="激活邮箱",default=False)

    #3,用户的默认收货地址



    #4, 指定表名信息
    class Meta:
        db_table = "tb_users"





