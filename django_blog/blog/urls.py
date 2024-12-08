from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.signin_view, name='login'),
    path('logout/', views.signout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('posts/', views.BlogPostsView.as_view(), name='posts'),
    path('post/new/', views.BlogPostsCreateView.as_view(), name='blogpost-create'),
    path('post/<int:pk>/', views.BlogPostsDetailsView.as_view(), name='blogpost-detail'),
    path('post/<int:pk>/update/', views.BlogPostsUpdateView.as_view(), name='blogpost-update'),
    path('post/<int:pk>/delete/', views.BlogPostsDeleteView.as_view(), name='blogpost-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name = 'edit_comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name= 'delete_comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tagposts'),
]
