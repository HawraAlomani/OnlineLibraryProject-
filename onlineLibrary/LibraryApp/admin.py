from django.contrib import admin
from .models import Book


class BooksAdmin(admin.ModelAdmin):
    list_display = ('namebook', 'publisher', 'description')
    list_filter = ('publisher',)
    # date_hierarchy = 'pub_date'
    search_fields = ('publisher',)


admin.site.register(Book, BooksAdmin)
