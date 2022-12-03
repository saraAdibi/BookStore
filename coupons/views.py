from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from cart.models import Cart
from .models import Coupon
from .forms import CouponApplyForm
# Create your views here.


@require_POST
def check_coupon(req):
    code = req.POST.get("code", None)

    c = Cart.objects.filter(id_user=req.user)
    cart_list = []
    grand = 0
    for i in c:
        # cart_list.append(
        #     [i.id_product.name, i.id_user.username, i.count, i.total_price, i.id, int(i.total_price / i.count),
        #      i.id_product.count])
        grand += i.total_price
    # context = {"products": cart_list, 'Grand_total': grand, "basketqty": i.count}

    if code:
        try:
            c = Coupon.objects.get(code=code)
            from decimal import Decimal
            t = (c.discount  * grand ) / 100
            grand -= t
            if c.active:
                c.active = False
                c.save()
                return JsonResponse({"check": True, "price": grand}, safe=True)
            else:
                return JsonResponse({"check": False, "price": grand}, safe=True)
        except Coupon.DoesNotExist:

            return JsonResponse({"check":False, "price": grand}, safe=True)


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid__from__lte=now, valid__to__gte=now, active=True)
            request.session['coupon_id'] = coupon_id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart')
            
