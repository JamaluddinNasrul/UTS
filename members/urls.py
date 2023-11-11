from django.urls import path
from . import views

urlpatterns = [
    # path('produk' , views.produk, name='produk'),
    # path('kategori' , views.kategori, name='kategori'),
    path('home' , views.home, name='home'),
]