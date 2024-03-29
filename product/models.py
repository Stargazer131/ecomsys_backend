import random
from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1, blank=True)
    image = models.ImageField(upload_to='image/product_images/', null=True, blank=True)
    type = models.CharField(max_length=20, choices=[
        ('book', 'book'), ('clothes', 'clothes'), ('mobile', 'mobile')
    ])
    is_active = models.BooleanField(default=True)


    class Meta:
        app_label = 'product'
        db_table = 'products'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('catalog_product', kwargs={'product_slug': self.slug})
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Product)
        super().save(*args, **kwargs)


def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id