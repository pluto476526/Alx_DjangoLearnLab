from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, FollowUserView, UnFollowUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('follow_user/', FollowUserView.as_view(), name='follow'),
    path('unfollow_user/', UnFollowUserView.as_view(), name='unfollow'),
]
