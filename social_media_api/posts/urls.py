from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, FeedAPIView, LikePostAPIView, UnlikePostAPIView



router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns += [
    path('feed/', FeedAPIView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostAPIView.as_view(), name='like'),
    path('<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='unlike'),
]
