from django.urls import path
from .views import LibraryDetails, books_list

urlpatterns = [
    path('books_list/', books_list, name='books_list')
    path('library/<int:pk>/', LibraryDetails.as_view, name='library_details')
]
