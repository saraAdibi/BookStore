from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class BankPartner(models.Model):
    username = models.CharField(max_length=25,default='',null=True,blank=True,verbose_name="نام کاربری")
    password = models.CharField(max_length=25,default='',null=True,blank=True,verbose_name="رمز عبور")
    merchant_code = models.CharField(max_length=60,verbose_name='کد مرچنت')
    token = models.CharField(max_length=100,verbose_name='توکن')   
    bank_name = models.CharField(max_length=60,verbose_name='نام بانک')
