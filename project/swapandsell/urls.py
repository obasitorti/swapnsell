from django.urls import path
from .import views

app_name = 'swapandsell'

urlpatterns = [
    path('', views.index, name='index'),
    path('allgadgets/', views.all_gadgets, name='all_gadgets'),
    path('addproduct/', views.add_product, name='add_product'),
]