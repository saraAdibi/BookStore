from django.contrib import admin
from .models import Coupon
# Register your models here.


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_form', 'valid_to', 'discount', 'active']
    list_filter = ['code', 'valid_form', 'valid_to']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
