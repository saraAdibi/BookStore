from django.shortcuts import redirect, render
from .models import Factors, FactorProducts
from cart.models import Cart
from products.models import products
from django.http import Http404
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


# Create your views here.

def index(req):
    if req.user.is_authenticated:
        carts = Cart.objects.filter(id_user=req.user).exists()
        if carts is False:
            return render(req, 'cart/index.html', {"error": "لطفا ابتدا کالایی انتخاب کنید"})
        else:
            carts = Cart.objects.filter(id_user=req.user)
            price = 0
            for c in carts:
                price += int(c.total_price)
            fac = Factors()
            fac.id_user = req.user
            fac.state = 1
            fac.total_price = price
            fac.save()
            for c in carts:
                product = products.objects.get(id=c.id_product.id)
                product.count -= c.count
                product.save()
                f_p = FactorProducts()
                f_p.id_factor = fac
                f_p.id_products = c.id_product
                f_p.count = c.count
                f_p.total_price = c.total_price
                f_p.save()
            list_of_fp = []
            fp = FactorProducts.objects.filter(id_factor=fac)
            for i in fp:
                list_of_fp.append(
                    [i.id_products.name, i.count, i.total_price, int(i.total_price / i.count), i.id_products.id])
            factor = [fac.id_user.username, fac.payment_date, fac.state, fac.create_date, fac.total_price, fac.id]
            carts.delete()

            return render(req, "factor/index.html", {"fp": list_of_fp, "f": factor})
    else:
        return render(req, "account/account.html", {'error': 'لطفا ابتدا وارد اکانت خود شوید'})


def factorview(req, id_factor):
    if req.user.is_authenticated:
        fp = FactorProducts.objects.filter(id_factor=id_factor)
        list_of_fp = []
        for i in fp:
            list_of_fp.append(
                [i.id_products.name, i.count, i.total_price, int(i.total_price / i.count), i.id_products.id])
        factor = Factors.objects.get(id=id_factor)
        f_list = [factor.id_user.username, factor.payment_date, factor.state, factor.create_date, factor.total_price,
                  id_factor]

        return render(req, "factor/index.html", {"fp": list_of_fp, 'f': f_list})
    else:
        return render(req, "account/account.html", {'error': 'لطفا ابتدا وارد اکانت خود شوید'})


def listfactors(req):
    count = 0
    from cart.models import Cart
    c = Cart.objects.filter(id_user=req.user)
    if c.exists():
        c = Cart.objects.filter(id_user=req.user)
        for i in c:
            count = i.count
    if req.user.is_authenticated:
        factors = Factors.objects.filter(id_user=req.user)
        f_list = []
        for f in factors:
            f_list.append([f.id_user.username, f.payment_date, f.state, f.create_date, f.total_price, f.id])
        return render(req, "factor/factors.html", {"factors": f_list, "basketqty": count})

    else:
        return render(req, "account/account.html", {'error': 'لطفا ابتدا وارد اکانت خود شوید'})


def deleteFactor(req, id_factor):
    f = Factors.objects.get(id=id_factor)
    if f.state != 3:
        fp = FactorProducts.objects.filter(id_factor=f)
        for p in fp:
            product = products.objects.get(id=p.id_products.id)
            product.count += int(p.count)
            product.save()
        f.delete()
        return redirect("listFactors")
    else:
        factors = Factors.objects.filter(id_user=req.user)
        f_list = []
        for f in factors:
            f_list.append([f.id_user.username, f.payment_date, f.state, f.create_date, f.total_price, f.id])
        return render(req, "factor/factors.html", {"factors": f_list, "error": "فاکتور پرداخت شده قابل حذف نیست"})


def state_change(req, id_factor):
    if req.user.is_authenticated:
        f = Factors.objects.get(id=id_factor)
        f.state = 3
        f.save()
        return redirect('listFactors')
    else:
        return Http404()
