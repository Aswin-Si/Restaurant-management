from django.db import models

# Create your models here.
class ReservationDb(models.Model):
    Date = models.CharField(max_length=100, null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Person = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank= True)

class SignupDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    EmailId = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    RepeatedPassword = models.CharField(max_length=100, null=True, blank=True)

class CartDb(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)

class CheckoutDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Items = models.ManyToManyField(CartDb, related_name='checkout_items',blank = True)
