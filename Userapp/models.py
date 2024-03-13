from django.db import models
from Sellerapp.models import *
from Adminapp.models import *


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user_table'


class UserImage(models.Model):
    image_id = models.IntegerField(primary_key=True, default=None)
    image = models.ImageField(upload_to='images/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for User: {self.user_id.user_name}"

    class Meta:
        db_table = 'user_image_table'


class UserAddress(models.Model):
    house_id = models.AutoField(primary_key=True)
    house_name = models.CharField(max_length=20, null=True)
    house_number = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    post = models.CharField(max_length=20, null=True)
    pin = models.CharField(max_length=20, null=True)
    landmark = models.CharField(max_length=20, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    city_name = models.ForeignKey(LocationCity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Address for User: {self.user_id}"


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True, default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'order_table'


class UserCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart item for {self.user_id.user_name}: {self.product_id.product_name}"


class Wishlist(models.Model):
    list_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist item for {self.user_id.user_name}: {self.product_id.product_name}"

    class Meta:
        db_table = 'wishlist_table'


class ReviewRating(models.Model):
    review_id = models.AutoField(primary_key=True, default=None)
    review = models.TextField()
    rating = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"ReviewRating item for"

    class Meta:
        db_table = 'review_rating_table'

