from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boutique_myan/categoria/<int:id_categoria>/', views.categoria, name="categoria"),
    path('boutique-myan/<int:id>/', views.produto, name="produto" ),
]