from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Category_image", null=True, blank=True)
class ProductDb(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    ProductPrice = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    ProductImage = models.ImageField(upload_to="Product_pic", null=True, blank=True)

class ContactDb(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    EmailId = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.ImageField(null=True, blank=True)
    Message = models.CharField(max_length=300, null=True, blank=True)