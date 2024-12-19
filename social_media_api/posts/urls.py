from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('', include(router.urls)),
]
