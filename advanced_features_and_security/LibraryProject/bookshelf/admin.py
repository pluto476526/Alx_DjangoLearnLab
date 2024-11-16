from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

    def publication_year(self, obj):
        return obj.published_date.year
    
    publication_year.short_description = 'Publication Year'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('username', 'date_of_birth', 'profile_photo', 'is_staff')
    list_editable = ('is_staff',)

    list_filter = ('is_staff', 'is_active')
    search_fields = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Special Dates', {'fields': ('last_login',)})
    )

try:
    admin.site.unregister(CustomUser)

except admin.sites.NotRegistered:
    pass

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Book, BookAdmin)
