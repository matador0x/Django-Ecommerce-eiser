from django.db import models
from django.urls import reverse

# Create your models here.



class Category(models.Model):

    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural =  'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shopy:shop", args=[self.slug])

class Brand(models.Model):

    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural =  'brands'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shopy:shop", args=[self.slug])

class Product(models.Model):

    category    = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand       = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE)
    name        = models.CharField(max_length=100, null=True)

    slug        = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=1500, blank=True)
    image       = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price  = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available   = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shopy:product_details", args=[self.id ,self.slug])