from django.urls import path
from .views import (
    ProfileListView,
    ProfileDetailView,
    ProfileUpdateView,
    RegisterView,
    ProfileDeleteView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]
