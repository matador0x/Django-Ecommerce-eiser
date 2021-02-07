from django.contrib import admin
from .models import Category, Product, Brand
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sale_price','available', 'created', 'updated']
    list_filter  = ['available', 'created', 'updated']
    list_editable = ['price', 'sale_price', 'available']
    prepopulated_fields = {'slug': ('name',)}
