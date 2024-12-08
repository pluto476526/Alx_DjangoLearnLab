from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.signin_view, name='login'),
    path('logout/', views.signout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('posts/', views.BlogPostsView.as_view(), name='posts'),
    path('posts/new/', views.BlogPostsCreateView.as_view(), name='blogpost-create'),
    path('posts/<int:pk>/', views.BlogPostsDetailsView.as_view(), name='blogpost-detail'),
    path('posts/<int:pk>/edit/', views.BlogPostsUpdateView.as_view(), name='blogpost-update'),
    path('posts/<int:pk>/delete/', views.BlogPostsDeleteView.as_view(), name='blogpost-delete'),
]
