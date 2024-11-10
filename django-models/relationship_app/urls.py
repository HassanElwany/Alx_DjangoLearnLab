from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView  
from .views import LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
    path('register/', views.register, name='register'),
]
