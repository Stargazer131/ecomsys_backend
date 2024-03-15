from django.contrib import admin
from book.models import Book, Genre, Author, Publisher, BookGenre


class BookGenreInline(admin.TabularInline):
    model = BookGenre
    exclude = ('id',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('product_name',)  # Use the actual field name from Product
    list_display_links = ('product_name',)
    list_per_page = 20
    ordering = ['product__name']
    search_fields = ['product__name']

    def product_name(self, obj):
        return obj.product.name

    inlines = [BookGenreInline]  # Add inline for BookGenre


class GenreAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Genre, GenreAdmin, using='product_db')


class AuthorAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Author, AuthorAdmin, using='product_db')


class PublisherAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Publisher, PublisherAdmin, using='product_db')