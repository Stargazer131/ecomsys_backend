from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
        help_text='Unique value for Product URL, created from name.'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1, blank=True)
    image = models.ImageField(upload_to='image/product_images/', null=True, blank=True)
    type = models.CharField(max_length=20, choices=[('book', 'book'), ('clothes', 'clothes'), ('mobile', 'mobile')])
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'product'
        db_table = 'products'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catalog_product', kwargs={'product_slug': self.slug})
    

class Book(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, primary_key=True)
    publish_year = models.IntegerField(default=2020, blank=True)
    genres = models.ManyToManyField('Genre')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books')

    class Meta:
        app_label = 'product'
        db_table = 'books'
        ordering = ['product__name']

    def __str__(self):
        return self.product.name
    
    def get_absolute_url(self):
        return reverse('catalog_book', kwargs={'book_slug': self.product.slug})


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
        help_text='Unique value for Genre URL, created from name.'
    )
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'product'
        db_table = 'genres'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('book_genre', kwargs={'genre_slug': self.slug})
    

class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
        help_text='Unique value for author URL, created from name.'
    )
    bio = models.TextField()
    birthday = models.DateField()
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ])
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'product'
        db_table = 'authors'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('book_author', kwargs={'author_slug': self.slug})
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
        help_text='Unique value for author URL, created from name.'
    )
    address = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'product'
        db_table = 'publishers'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('book_publisher', kwargs={'publisher_slug': self.slug})
    