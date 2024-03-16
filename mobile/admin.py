from django.contrib import admin
from mobile.models import Mobile, MobileType


# Register your models here.
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('product_name',)  # Use the actual field name from Product
    list_display_links = ('product_name',)
    list_per_page = 20
    ordering = ['product__name']
    search_fields = ['product_name']

    def product_name(self, obj):
        return obj.product.name


@admin.register(MobileType)
class MobileTypeAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    prepopulated_fields = {'slug': ('name',)}
