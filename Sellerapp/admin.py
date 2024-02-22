from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Specification)
admin.site.register(Brand)
