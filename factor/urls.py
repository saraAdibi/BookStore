from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="factor"),
    path("factors", views.listfactors, name="listFactors"),
    path("delete/<int:id_factor>", views.deleteFactor, name="delete_factor"),
    path('factorview/<int:id_factor>', views.factorview, name="factorview"),
    path('statechange/<int:id_factor>', views.state_change, name='statechange'),

]
