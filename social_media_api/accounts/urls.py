from django.urls import path
from .views import RegisterView, CustomObtainAuthToken


urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', CustomObtainAuthToken.as_view(), name='login'),
]
