from django.contrib import admin
from clothes.models import ClothingItem, Manufacturer, Style, ClothingItemStyle


# Register your models here.
class ClothingItemStyleInline(admin.TabularInline):
    model = ClothingItemStyle
    # exclude = ('id',)


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('product_name',)  # Use the actual field name from Product
    list_display_links = ('product_name',)
    list_per_page = 20
    ordering = ['product__name']
    search_fields = ['product_name']

    def product_name(self, obj):
        return obj.product.name
    
    inlines = [ClothingItemStyleInline]


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
