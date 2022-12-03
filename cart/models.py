from django.db import models
from django.db.models.deletion import CASCADE
from django.forms import ModelForm

from products.models import products
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    id_product = models.ForeignKey(products, verbose_name='محصولات', on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, verbose_name="نام کاربری", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    total_price = models.PositiveIntegerField(verbose_name="مبلغ نهایی")


class PromoCode(ModelForm):
    code = models.FloatField(max_length=15)
    discount = models.FloatField(max_length=15)
