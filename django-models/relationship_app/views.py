from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test

from .models import Library, Book

# Create your views here.


def is_admin(user):
    return user.profile.role == 'admin'


def is_librarian(user):
    return user.profile.role == 'librarian'


def is_member(user):
    return user.profile.role == 'member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

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