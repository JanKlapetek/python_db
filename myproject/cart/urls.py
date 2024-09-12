from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('edit/<int:item_id>/', views.edit_cart_item, name='edit_cart_item'),
    path('delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('', views.view_cart, name='view_cart'),
]