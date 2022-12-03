from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import categories, products, subcategories


def index(req):
    # todo: check login for specialist
    from .models import products, categories
    if req.user and req.user.is_authenticated:
        # select all categories
        cat = categories.objects.all()
        sub = subcategories.objects.all()
        list_of_cat = []
        list_of_sub = []
        for i in cat:
            list_of_cat.append([i.id, i.name, i.slug])
        for i in sub:
            list_of_sub.append([i.name, i.parent.name])
        # select all products
        p = products.objects.filter(deleted=False)
        list_of_product = []
        count = 0
        from cart.models import Cart
        c = Cart.objects.filter(id_user=req.user)
        if c.exists():
            c = Cart.objects.filter(id_user=req.user)
            for i in c:
                count = i.count
        for i in p:

            list_of_product.append([i.name, i.count, i.price, i.category.name, i.id, i.slug, i.image])
        return render(req, "product/index.html",
                      {"list": list_of_product, "categories": list_of_cat, "subcategories": list_of_sub, "basketqty":count})
    else:
        return redirect("login")


# def image_page(request):
#     image = products.objects.all()
#     return render(request, 'product/index.html', {'image': image})


def get_product(req, id_product):
    p = products.objects.get(id=id_product)
    product_info = [p.name, p.price, p.count, p.category.name, id_product, p.description, p.image]
    count = 0
    from cart.models import Cart
    c = Cart.objects.filter(id_user=req.user)
    if c.exists():
        c = Cart.objects.filter(id_user=req.user)
        for i in c:
            count = i.count
    return render(req, "product/info.html", {"info": product_info, "basketqty":count})
