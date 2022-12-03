from django.urls import path
from django.urls.conf import include
from . import views

# profile = [
#     path('edit', views.edit, name="edit"),
#     path('delete', views.delete, name="delete"),
# ]

urlpatterns = [
    path('', views.account, name="account"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.login, name="login"),
    path('logout', views._logout, name="logout")

]