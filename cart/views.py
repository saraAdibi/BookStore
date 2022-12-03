from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from cart.models import Cart
from django.http.response import JsonResponse
from coupons.forms import CouponApplyForm
from products.models import products
from .basket import Basket


# Create your views here.
def basket_summary(request):
    basket = Cart(request)
    coupon_apply_form = CouponApplyForm()
    return render(request, 'basket/summary.html', {'basket': basket, 'coupon_apply_form':coupon_apply_form})


def basket_add(request):
    basket = Cart(request)
    if request.POST.get('action') == 'post':
        product_qty = int(request.POST.get('productqty'))
        basket.add(qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def index(req):
    if req.user.is_authenticated:
        c = Cart.objects.filter(id_user=req.user).exists()
        if c is True:
            c = Cart.objects.filter(id_user=req.user)
            cart_list = []
            grand = 0
            for i in c:
                cart_list.append(
                    [i.id_product.name, i.id_user.username, i.count, i.total_price, i.id, int(i.total_price / i.count),
                     i.id_product.count])
                grand += i.total_price
            context = {"products": cart_list, 'Grand_total': grand, "basketqty":i.count, }
            return render(req, 'cart/index.html', context,)

        else:
            return render(req, 'cart/index.html', {"error": "سبد خرید خالی میباشد", "basketqty":0})
    else:
        return render(req, "account/account.html", {'error': 'لطفا ابتدا وارد اکانت خود شوید'})


def add(req, product_id, num):
    if req.user.is_authenticated:
        try:
            carts = Cart.objects.get(id_product=product_id, id_user=req.user)
        except:
            carts = None
        try:
            p = products.objects.get(id=product_id)
        except:
            return Http404()
        if carts is None and p.count > 0:
            c = Cart()
            c.id_product = p
            c.id_user = req.user
            c.count = 1
            c.total_price = int(p.price)
            c.save()
            p.count -= 1
            p.save()
            if num is 1:
                return redirect('product')
            elif num is 2:
                return HttpResponseRedirect(reverse("get_product", kwargs={"id_product": product_id}))
        elif carts is not None and p.count > 0:
            carts.count += 1
            carts.total_price += int(p.price)
            carts.save()
            p.count -= 1
            p.save()
            if num is 1:
                return redirect('product')
            elif num is 2:
                return HttpResponseRedirect(reverse("get_product", kwargs={"id_product": product_id}))
    else:
        return render(req, "account/account.html", {'error': 'لطفا ابتدا وارد اکانت خود شوید'})


def addCart(req, id_cart):
    c = Cart.objects.get(id=id_cart)
    p = c.id_product
    if p.count > 0:
        c.count += 1
        c.total_price += int(p.price)
        p.count -= 1
        c.save()
        p.save()
        return redirect('cart')


def delete(req, id_cart):
    try:
        c = Cart.objects.get(id=id_cart)
    except:
        return Http404()
    p = c.id_product
    c.count -= 1
    c.total_price -= int(p.price)
    p.count += 1
    c.save()
    p.save()
    if c.count == 0:
        c.delete()
    return redirect('cart')

# def pre_factor(req):
#     c = Cart.objects.filter(id_user=req.user)
#     Cart_list = []
#     price = 0
#     for i in c:
#         price += int(i.total_price)

#         Cart_list.append([i.id_product.name,i.id_user.username,i.count,i.total_price,i.id])

#     return render(req,'cart/preFactor.html',{"products":Cart_list,"total_price":price})


def basket_add(request):
    basket = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        # p = products.objects.filter(id=product_id)
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Cart, id=product_id)
        # basket.id_product = p
        # basket.id_user = request.user
        basket.add(product=product, qty=product_qty)

        basketqty = basket.count()
        print(basketqty)
        response = JsonResponse({'qty': basketqty})
        return response



