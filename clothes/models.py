from django.db import models
from django.urls import reverse


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
    )
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50) 
    description = models.TextField()


    class Meta:
        app_label = 'product'
        db_table = 'manufacturers'
        ordering = ['name']
    
    
    def get_absolute_url(self):
        return reverse('catalog_manufacturer', kwargs={'manufacturer_slug': self.slug})


    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(
        max_length=50, unique=True, 
    )


    class Meta:
        app_label = 'product'
        db_table = 'styles'
        ordering = ['name']
        

    def get_absolute_url(self):
        return reverse('clothes_style', kwargs={'style_slug': self.slug})


    def __str__(self):
        return self.name


class ClothingItem(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, primary_key=True)
    manufacturer_date = models.DateField()
    styles = models.ManyToManyField('Style')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='clothing_items')


    class Meta:
        app_label = 'product'
        db_table = 'clothes'
        ordering = ['product__name']


    def __str__(self):
        return self.product.name
    
    
    def get_absolute_url(self):
        return reverse('catalog_clothes', kwargs={'clothes_slug': self.product.slug})