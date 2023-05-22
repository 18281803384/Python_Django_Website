from django.db import models


# Create your models here.
class user(models.Model):
    """
    用户表
    """
    user_name = models.CharField(verbose_name='用户名',max_length=64)
    user_password = models.CharField(verbose_name='密码',max_length=64)
    create_time = models.CharField(verbose_name="创建时间", max_length=19)
    update_time = models.CharField(verbose_name="修改时间", max_length=19, null=True, blank=True, default='')