from django.contrib import admin
from bookshelf.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

    def publication_year(self, obj):
        return obj.published_date.year
    
    publication_year.short_description = 'Publication Year'

admin.site.register(Book, BookAdmin)
