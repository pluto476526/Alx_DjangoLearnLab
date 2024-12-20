"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from relationship_app import views
from bookshelf import views as v
from relationship_app.views import LibraryDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_list/', views.books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetails.as_view(), name='library_details'),
    path('edit_book/<int:pk>/', v.edit_book, name='edit_book'),
    path('create_book/', v.create_book, name='create_book'),
    path('all_books/', v.book_list, name='all_books'),
    path('delete_book/<int:pk>', v.delete_book, name='delete_book'),
    path('form_example/', v.form_example, name='form_example'),
]
