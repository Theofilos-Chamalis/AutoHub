from django.conf import settings
from django.db import models
from django.utils import timezone


class Category1(models.Model):
    Fuel = models.CharField(max_length=15)
    desc = models.TextField()

    def __str__(self):
        return self.Fuel


class Category2(models.Model):
    Transmission = models.CharField(max_length=15)
    desc = models.TextField()

    def __str__(self):
        return self.Transmission


class Category3(models.Model):
    Year_model = models.CharField(max_length=15)

    def __str__(self):
        return self.Year_model


class Category4(models.Model):
    Cat_car = models.CharField(max_length=15)
    desc = models.TextField()

    def __str__(self):
        return self.Cat_car


class Category5(models.Model):
    country = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.country


class Seller(models.Model):
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    city = models.CharField(null=True, max_length=10)
    post_code = models.CharField(null=True, max_length=5)
    photo = models.ImageField(null=True)
    Resume = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    mob_phone = models.CharField(null=True, max_length=15)
    birth_date = models.DateField()
    Email = models.CharField(max_length=25)
    working_brand = models.CharField(null=True, max_length=50)

    def __str__(s):
        return s.last_name


class Manufacturer(models.Model):
    brand = models.CharField(max_length=50, null=True)
    country = models.ForeignKey(Category5, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    established = models.DateField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    cover = models.ImageField(null=True)
    cover2 = models.ImageField(null=True)

    def __str__(f):
        return f.brand


class Car(models.Model):
    brand = models.ForeignKey(Manufacturer, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=15, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cover = models.ImageField(null=True)
    cover1 = models.ImageField(null=True)
    cover2 = models.ImageField(null=True)
    Fuel = models.ForeignKey('Category1', null=True, on_delete=models.CASCADE)
    Transmission = models.ForeignKey('Category2', null=True, on_delete=models.CASCADE)
    Year = models.ForeignKey('Category3', null=True, on_delete=models.CASCADE)
    Car_Category = models.ForeignKey('Category4', null=True, on_delete=models.CASCADE)
    video = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title
