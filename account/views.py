from django.http.response import Http404
from django.shortcuts import render, redirect


# Create your views here.
def account(req):
    if req.user and req.user.is_authenticated:
        username = req.user.username
        first_name = req.user.first_name
        last_name = req.user.last_name
        return render(req, 'account/dashboard.html', {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
        })
    else:
        return redirect("login")
    # if req.method == "GET":
    #     return render(req, "account/account.html", )


def dashboard(req):
    if not req.user or not req.user.is_authenticated:
        return redirect("login")

    count = 0
    from cart.models import Cart
    c = Cart.objects.filter(id_user=req.user)
    if c.exists():
        c = Cart.objects.filter(id_user=req.user)
        for i in c:
            count = i.count
    if req.user.is_authenticated:
        return render(req, "account/dashboard.html", {"basketqty": count})


def login(req):
    if req.method == 'POST':
        from django.contrib.auth import authenticate, login
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect("dashboard")
        else:
            return render(req, "account/Login.html", {"error": "ورود نامعتبر"})

    elif req.method == 'GET':
        return render(req, 'account/Login.html')
    else:
        return Http404()


def register(req):
    if req.method == 'POST':
        from django.contrib.auth.models import User

        full_name = req.POST.get('fullname', None)
        if isinstance(full_name, str) and full_name.index(" ") > 0:
            first_name, last_name = full_name.split()

        username = req.POST['username']
        password = req.POST['password']
        confirm_pass = req.POST['confirm_password']
        email = req.POST['email']
        if password != confirm_pass:
            return render(req, "account/register.html", {"error": "رمز خود را دوباره وارد کنید"})
        try:
            from django.contrib.auth.models import User
            User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            pass
        else:
            return render(req, "account/register.html", {"error": "این یوزر قبلا ساخته شده"})

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('login')

    elif req.method == 'GET':
        if req.user.is_authenticated:
            return redirect("dashboard")
        else:
            return render(req, 'account/register.html')
    else:
        return Http404()


def _logout(req):
    if req.user.is_authenticated:
        from django.contrib.auth import logout
        logout(req)

    return redirect("account")
