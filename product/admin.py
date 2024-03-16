from django.contrib import admin
from product.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'type']
    prepopulated_fields = {'slug': ('type', 'name')}
