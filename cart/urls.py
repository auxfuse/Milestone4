from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_cart, name='view-cart'),
    path('add-to-cart/<membership_id>', views.add_to_cart, name='add-to-cart'),
    path('del-from-cart/<membership_id>', views.del_from_cart,
         name='del-from-cart')
]
