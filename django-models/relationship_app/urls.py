from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register, admin_view, librarian_view, member_view

urlpatterns = [
    path('books_list/', views.list_books, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view, name='library_details'),
    path('login/', LoginView.as_view(template_name='login')),
    path('logout/', LogoutView.as_view(template_name='logout')),
    path('register/', views.register, name='register'),
    path('admin/', views.Admin, name='admin_view'),
    path('librarian/', views.Librarian, name='librarian_view'),
    path('member/', views.Member, name='member_view'),
]
