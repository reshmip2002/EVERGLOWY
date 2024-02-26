from django.urls import path
from . import views



urlpatterns = [
    path('', views.seller_home, name='home'),
    # path('seller_login',views.seller_login, name='login'),


]
