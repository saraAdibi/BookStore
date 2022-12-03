from django.contrib import admin
from django.contrib.admin.sites import site

from factor.models import FactorProducts, Factors
from transaction.models import Transactions


# Register your models here.
admin.site.register(Transactions)