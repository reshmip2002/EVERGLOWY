from django.db import models

class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True, default=None)
    brand_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.brand_name



# Create your models here.

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True, default=None)
    seller_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    experience = models.CharField(max_length=20, null=True)
    license_number = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.seller_name

    class Meta:
        db_table = "seller_table"

class Category(models.Model):
    main_category_id = models.IntegerField(primary_key=True, default=None)
    main_category_name = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.main_category_name

    class Meta:
        db_table = "Category_table"


class SubCategory(models.Model):
    sub_category_id = models.IntegerField(primary_key=True, default=None)
    sub_category_name = models.CharField(max_length=50, null=True)
    main_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name

    class Meta:
        db_table = "Subcategory_table"


class SubSubCategory(models.Model):
    sub_sub_category_id = models.IntegerField(primary_key=True, default=None)
    sub_sub_category_name = models.CharField(max_length=50, null=True)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_sub_category_name

    class Meta:
        db_table = "Sub2category_table"

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, default=None)
    product_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    expiry_date = models.DateField()
    quantity = models.CharField(max_length=20, null=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    main_category_id = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=50, default='Active')
    created_at = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.product_name


    class Meta:

        db_table = 'product_table'


class ProductImage(models.Model):
    image_id = models.IntegerField(primary_key=True, default=None)
    image = models.ImageField(upload_to='images/')
    product_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for Product: {self.product_id.product_name}"

    class Meta:
        db_table = 'product_image_table'


class Specification(models.Model):
    specification_id = models.IntegerField(primary_key=True, default=None)
    specification_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    expiry_date = models.DateField()
    number_of_products = models.CharField(max_length=20, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.specification_name

    class Meta:
        db_table = 'specification_table'
