from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(UserImage)
admin.site.register(UserAddress)
admin.site.register(Order)
admin.site.register(UserCart)
admin.site.register(Wishlist)
admin.site.register(ReviewRating)