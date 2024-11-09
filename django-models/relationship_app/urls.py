from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView

urlpatterns = [
    path('books_list/', list_books, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view, name='library_details'),
    path('login/', LoginView.as_view, template_name='login'),
    path('logout/', LogoutView.as_view, template_name='logout'),
]
