from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('product_details/', product_details, name='product_details'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('blog_single/', blog_single, name='blog_single'),
    path('login/', log_in, name='log_in'),
    path('register/', register, name='register'),
    path('log_out/', log_out, name='log_out'),



    # password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'),
         name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),

]
