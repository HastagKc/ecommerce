from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('checkout/', chaekout, name='chaekout'),
    path('contact/', contact, name='contact'),
    path('product_details/', product_details, name='product_details'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('blog_single/', blog_single, name='blog_single'),
    path('login/', log_in, name='log_in'),
    path('register/', register, name='register'),
]
