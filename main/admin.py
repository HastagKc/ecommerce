from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register([Category, Subcategory, Product])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image1', 'image2', 'image3', 'category', 'sub_category',
                    'name', 'desc', 'Mark_price', 'price', 'discount_percentage', 'date']
