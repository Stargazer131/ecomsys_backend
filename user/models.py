from django.db import models
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, 
    )
    birthday = models.DateField()
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=True)


    class Meta:
        app_label = 'user'
        db_table = 'users'
        ordering = ['username']


    def __str__(self):
        return self.username
    
    
    def get_absolute_url(self):
        return reverse('catalog_user', kwargs={'user_slug': self.slug})

