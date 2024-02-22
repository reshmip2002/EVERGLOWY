from django.db import models
from Sellerapp.models import Product


# Create your models here.

class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True, default=None)
    admin_name = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.admin_name

    class Meta:
        db_table = "Admin_table"


class LocationState(models.Model):
    state_id = models.IntegerField(primary_key=True, default=None)
    state_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = "state_table"


class LocationDistrict(models.Model):
    district_id = models.IntegerField(primary_key=True, default=None)
    district_name = models.CharField(max_length=50, null=True)
    state_id = models.ForeignKey(LocationState, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name

    class Meta:
        db_table = "district_table"


class LocationCity(models.Model):
    city_id = models.IntegerField(primary_key=True, default=None)
    city_name = models.CharField(max_length=50, null=True)
    district_id = models.ForeignKey(LocationDistrict, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = "city_table"


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True, default=None)
    event_name = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = "event_table"


class Offer(models.Model):
    offer_id = models.IntegerField(primary_key=True, default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    discount = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"Offer for {self.product_id.product_name} at {self.event_id.event_name}"

    class Meta:
        db_table = "offer_table"


