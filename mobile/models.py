from django.db import models
from django.urls import reverse
from product.models import random_id


# Create your models here.
class MobileType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(
        max_length=50, unique=True, 
    )
    
    
    class Meta:
        app_label = 'product'
        db_table = 'mobile_types'
        ordering = ['name']
        
        
    def get_absolute_url(self):
        return reverse('mobile_type', kwargs={'type_slug': self.slug})


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(MobileType)
        super().save(*args, **kwargs)


class Mobile(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, primary_key=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='mobiles')
    mobile_type = models.ForeignKey('MobileType', on_delete=models.CASCADE, related_name='mobiles')
    release_date = models.DateField()
    rom_size = models.IntegerField() # in MB
    ram_size = models.IntegerField()
    display_resolution = models.CharField(max_length=50)
    battery_capacity = models.IntegerField() # in MA
    chip = models.CharField(max_length=50)


    class Meta:
        app_label = 'product'
        db_table = 'mobiles'
        ordering = ['product__name']


    def __str__(self):
        return self.product.name
    
    
    def get_absolute_url(self):
        return reverse('catalog_mobile', kwargs={'mobile_slug': self.product.slug})
