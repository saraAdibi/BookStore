from django.urls import path, include, re_path
from . import views
from django.contrib import admin
from django.urls import path, include
# from image import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="product"),
    # path('add', views.add, name="add_product"),
    # path('delete/<int:id_cat>', views.delete, name="delete_product"),
    # path('edit/<int:id_cat>', views.edit, name="edit_product"),
    # path('get/subcategories', views.get_subcategories, name="get_subcategories"),
    path('get/product/<int:id_product>', views.get_product, name="get_product"),
    path('admin/', admin.site.urls),
    path('', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)