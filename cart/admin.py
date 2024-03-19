from django.contrib import admin
from cart.models import CartItem

# Register your models here.
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-date_added']
