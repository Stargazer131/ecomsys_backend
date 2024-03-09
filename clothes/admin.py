from django.contrib import admin
from clothes.models import ClothingItem, Manufacturer, Style

# Register your models here.
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('product_name',)  # Use the actual field name from Product
    list_display_links = ('product_name',)
    list_per_page = 20
    ordering = ['product__name']
    search_fields = ['product_name']

    def product_name(self, obj):
        return obj.product.name

admin.site.register(ClothingItem, ClothingItemAdmin, using='product_db')


class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Style, StyleAdmin, using='product_db')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Manufacturer, ManufacturerAdmin, using='product_db')