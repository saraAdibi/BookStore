from django.conf.urls import url

# from Store.urls import urlpatterns
from .import views

urlpatterns = [
    url(r'^apply/$', views.coupon_apply, name='apply'),
    url(r'^check_coupon/$', views.check_coupon, name='check_coupon'),
]