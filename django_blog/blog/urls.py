from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.signin_view, name='login'),
    path('logout/', views.signout_view, name='logout'),
    path('posts/', views.posts_view, name='posts'),
    path('profile/', views.profile_view, name='profile'),
]
