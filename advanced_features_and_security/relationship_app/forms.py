# relationship_app/forms.py
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date',
                  'isbn', 'cover_image']  # Include the fields you need
