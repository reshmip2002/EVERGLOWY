from django.db import models
from Sellerapp.models import *  # Assuming Product is imported from Sellerapp.models
from Adminapp.models import *   # Assuming LocationCity is imported from Adminapp.models
from django.utils import timezone


class User(models.Model):
    """
    Represents a user of the platform.

    Attributes:
        user_name (str): The name of the user.
        email (str): The email address of the user. Primary key.
        phone_number (str): The phone number of the user.
        password (str): The password of the user.
    """

    # Fields
    user_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_name


class UserImage(models.Model):
    """
    Represents images associated with a user.

    Attributes:
        image_id (int): The ID of the image.
        image (ImageField): The image file.
        user_id (ForeignKey): The user associated with this image.
    """

    # Fields
    image_id = models.IntegerField(primary_key=True, default=None)
    image = models.ImageField(upload_to='images/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for User: {self.user_id.user_name}"


class UserAddress(models.Model):
    """
    Represents addresses associated with users.

    Attributes:
        house_id (int): The ID of the house.
        house_name (str): The name of the house.
        house_number (str): The house number.
        place (str): The place.
        post (str): The post.
        pin (str): The PIN code.
        landmark (str): The landmark.
        user_id (ForeignKey): The user associated with this address.
        city_name (ForeignKey): The city associated with this address.
    """

    # Fields
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
    """
    Represents an order made by a user.

    Attributes:
        order_id (int): The ID of the order.
        product_id (ForeignKey): The product in the order.
        quantity (str): The quantity of the product.
        user_id (ForeignKey): The user who made the order.
        status (str): The status of the order.
    """

    # Fields
    order_id = models.IntegerField(primary_key=True, default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.product_name


class UserCart(models.Model):
    """
    Represents items added to a user's cart.

    Attributes:
        cart_id (int): The ID of the cart item.
        product_id (ForeignKey): The product in the cart.
        quantity (int): The quantity of the product.
        user_id (ForeignKey): The user who added the item to the cart.
    """

    # Fields
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart item for {self.user_id.user_name}: {self.product_id.product_name}"


class Wishlist(models.Model):
    """
    Represents items added to a user's wishlist.

    Attributes:
        list_id (int): The ID of the wishlist item.
        product_id (ForeignKey): The product in the wishlist.
        user_id (ForeignKey): The user who added the item to the wishlist.
    """

    # Fields
    list_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist item for {self.user_id.user_name}: {self.product_id.product_name}"


class ReviewRating(models.Model):
    """
    Represents reviews and ratings given by users for products.

    Attributes:
        review_id (int): The ID of the review.
        review (str): The review text.
        rating (int): The rating given by the user.
        user_id (ForeignKey): The user who gave the review.
        product_id (ForeignKey): The product being reviewed.
    """

    # Fields
    review_id = models.AutoField(primary_key=True, default=None)
    review = models.TextField()
    rating = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"ReviewRating item for"


class RecentlyViewed(models.Model):
    """
    Represents products recently viewed by users.

    Attributes:
        user_id (ForeignKey): The user who viewed the product.
        product_id (ForeignKey): The product being viewed.
        viewed_at (DateTimeField): The timestamp when the product was viewed.
    """

    # Fields
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_id
