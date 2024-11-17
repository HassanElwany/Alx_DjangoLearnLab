from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

from django.db.models import Q



def search_books(request):
    query = request.GET.get('q')
    if query:
        # Using ORM and Q objects for safe query building
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        results = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'results': results})

@permission_required('books.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'book': book})

@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('view_books')
