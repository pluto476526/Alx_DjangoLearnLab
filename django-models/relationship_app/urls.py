from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books_list/', list_books, name='books_list')
    path('library/<int:pk>/', LibraryDetailView.as_view, name='library_details')
]
