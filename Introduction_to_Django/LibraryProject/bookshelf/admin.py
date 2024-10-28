from django.contrib import admin
from bookshelf.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    display = ('title', 'author', 'publication_year')
    items_filter = ('author', 'published_date')
    search = ('title', 'author')

    def pub_year(self, obj):
        return obj.published_date.year
    
    pub_year.short_description = 'Publication Year'
    pub_year.admin_order_field = 'published_date'

admin.site.register(Book, BookAdmin)
