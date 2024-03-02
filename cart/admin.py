from django.contrib import admin
from cart.models import CartItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-date_added']

admin.site.register(CartItem, CartItemAdmin, using='cart_db')