from django.urls import path
from .views import *

urlpatterns = [
    path('seller_signin/', seller_signInPage, name='seller_signin'),
    path('seller_logout/', seller_logoutPage, name='seller_logout'),
    path('seller_signup/', seller_signUpPage, name='seller_signup'),
    path('seller_profile/', seller_profilePage, name="seller_profile"),
    path('dashboard/', dashboard, name="dashboard"),
    path('products/', productsView, name="products"),
    path('product_details/<id>',  productDetailView, name="product_details"),
    path('category/', categoryView, name="category"),
    path('orders/', ordersView, name="orders"),
]
