from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.detail import DetailView

from .models import Library, Book

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'