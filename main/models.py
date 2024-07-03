from django.db import models
from ckeditor.fields import RichTextField
import re

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    image1 = models.ImageField(
        upload_to='product', blank=True)  # pip install pillow
    image2 = models.ImageField(
        upload_to='product', blank=True)  # pip install pillow
    image3 = models.ImageField(
        upload_to='product', blank=True)  # pip install pillow

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    desc = RichTextField(blank=True)
    Mark_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False)

    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price = self.Mark_price * (1 - self.discount_percentage / 100)
        self.name = self.name.capitalize()
        self.desc = re.sub(r'<[^>]*>', ' ', self.desc)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
