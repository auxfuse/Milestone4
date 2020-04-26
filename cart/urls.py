from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_cart, name='view-cart'),
    path('add-to-cart/<int:id>', views.add_to_cart,
         name='add-to-cart'),
    path('clear-cart/', views.clear_cart,
         name='clear-cart')
]
