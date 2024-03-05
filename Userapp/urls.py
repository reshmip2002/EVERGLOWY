from django.urls import path
from . import views
# from .views import add_to_cart
from .views import products
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/<int:id>', views.products, name='products'),
    path('cart', views.cart, name='cart'),
    path('dlt_product/<int:cart_id>', views.dlt_product, name='dlt_product'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('dlt_listproduct/<int:list_id>', views.dlt_listproduct, name='dlt_listproduct'),
    path('reviewrating/<int:product_id>', views.reviewrating, name='reviewrating'),
    path('category/<int:main_category_id>', views.category, name='category'),
    path('search', views.search, name='search'),
    path('offers', views.offers, name='offers'),
    path('brand', views.brand, name='brand'),
    path('all_brands', views.all_brands, name='all_brands'),
    path('buy', views.buy, name='buy'),
    path('checkout', views.checkout, name='checkout'),
    path('address', views.address, name='address'),
    path('profile', views.profile, name='profile'),
    path('address', views.address, name='address'),
    path('view_address', views.view_address, name='view_address'),
    path('edit_address/<int:house_id>', views.edit_address, name='edit_address'),
    path('dlt_address/<int:house_id>', views.dlt_address, name='dlt_address'),
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout',views.logout),
]
