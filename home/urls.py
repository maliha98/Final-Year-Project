from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home'),
    path('cart/', cartView, name='cart'),
    path('cart/<id>', addToCart, name='cart'),
    path('<id>', plusCart, name='pluscart'),
    path('minus/<id>', minusCart, name='minuscart'),
    path('remove/<id>', removeCart, name='removecart'),
    path('catgory/<id>', categoryView, name='category'),
    path('checkout/', checkout, name='checkout'),
    path('address_update/<id>', address_form, name='address_update'),
    path('payment/', payment, name='payment'),
    path('about/', aboutPage, name='about'),
]