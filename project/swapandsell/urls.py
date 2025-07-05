from django.urls import path
from .import views

app_name = 'swapandsell'

urlpatterns = [
    path('', views.index, name='index'),
    path('allgadgets/', views.all_gadgets, name='all_gadgets'),
    path('addproduct/', views.add_product, name='add_product'),
    path('allgadgets/<int:detail_id>/', views.detail, name='detail'),
    path('mygadgets/', views.my_gadgets, name='my_gadgets'),
    path('editproduct/<int:detail_id>/', views.edit_product, name='edit_product'),
    path('deleteproduct/<int:detail_id>/', views.delete_product, name='delete_product'),
]