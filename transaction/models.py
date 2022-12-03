from django.db import models
from ..bank_partner.models import BankPartner
from ..factor.models import Factors
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

trans_state = (
    (1, "پرداخت نشده"),
    (2, "در انتظار پرداخت"),
    (3, "پرداخت شده")
)

class Transactions(models.Model):
    id_bank_partner = models.ForeignKey(BankPartner, verbose_name="نام بانک", on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, verbose_name="نام کاربری", on_delete=models.CASCADE)
    id_factor = models.ForeignKey(Factors, verbose_name="شماره فاکتور", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="مبلغ")
    state = models.PositiveIntegerField(choices=trans_state, verbose_name="وضعیت پرداخت")
    payment_date = models.DateTimeField(default=datetime.now(), verbose_name="تاریخ پرداخت")
    create_date = models.DateTimeField(default=datetime.now(), verbose_name="تاریخ ایجاد")
    token = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name="توکن")
