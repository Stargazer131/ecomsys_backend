from django.contrib import admin
from user.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_display_links = ('username',)
    list_per_page = 20
    ordering = ['username']
    search_fields = ['username', 'email',]
    prepopulated_fields = {'slug': ('username',)}