from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, FollowUserView, UnFollowUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnFollowUserView.as_view(), name='unfollow'),
]
