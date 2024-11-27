from django.urls import path
from . views import ListView, DetailView, CreateView, UpdateView, DeleteView


urlpatterns = [
    path('books/', ListView.as_view(), name='books_list'),
    path('books/<int:pk>/', DetailView.as_view, name='details'),
    path('books/new/', CreateView.as_view(), name='new_book'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='update_book')
    path('books/<int:pk>/', DeleteView.as_view(), name='delete_book'),
]
