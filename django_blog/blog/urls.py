from django.urls import path
from .views import (
    ProfileListView,
    ProfileDetailView,
    ProfileUpdateView,
    RegisterView,
    ProfileDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,  # New view for creating comments
    CommentEditView,    # New view for editing comments
    CommentDeleteView,  # New view for deleting comments
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),

    # Post CRUD URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment CRUD URLs
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),  # For adding a comment
    path('comment/<int:pk>/edit/', CommentEditView.as_view(), name='comment_edit'),  # For editing a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),  # For deleting a comment
]
