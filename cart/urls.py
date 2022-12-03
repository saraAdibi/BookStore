from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:product_id>/<int:num>', views.add, name="add_to_cart"),
    path('delete/<int:id_cart>', views.delete, name="delete_cart"),
    path('addCart/<int:id_cart>', views.addCart, name="addCart"),
    # path('add_coupon/<code>', views.add_coupon, name="add_coupon"),
    # path('preFactor',views.pre_factor,name="pre_factor")
]
