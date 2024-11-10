from django.urls import path
from . import views
from .views import LogoutView, LoginView, LibraryDetailView
urlpatterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'), 
]