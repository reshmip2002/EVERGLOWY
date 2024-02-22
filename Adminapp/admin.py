from django.contrib import admin
from . models import *
from  Sellerapp.models import *
# Register your models here.

admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
admin.site.register(LocationState)
admin.site.register(LocationDistrict)
admin.site.register(LocationCity)
admin.site.register(Event)
admin.site.register(Offer)