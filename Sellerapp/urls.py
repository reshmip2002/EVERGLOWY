from django.urls import path
from . import views



urlpatterns = [

    path('', views.seller_home, name='home'),
    path('/seller_login',views.seller_login, name='login'),
    path('/seller_signup',views.seller_signup, name='signup'),
    path('/seller_logout',views.seller_logout, name='logout'),
    path('/seller_view_product',views.seller_viewproduct, name='viewproduct'),
    path('/seller_add_product',views.seller_addproduct, name='addproduct'),
    path('/seller_edit_product/<int:product_id>',views.seller_editproduct, name='editproduct'),
    path('/seller_delete_product',views.seller_deleteproduct, name='deleteproduct'),
    path('/seller_add_image',views.seller_add_image, name='addimage'),
    path('/seller_edit_image',views.seller_edit_image, name='editimage'),

]
