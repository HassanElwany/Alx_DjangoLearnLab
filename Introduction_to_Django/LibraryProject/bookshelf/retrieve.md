```markdown
# Retrieving the created Book instance
```python
python manage.py shell

>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title, book.author, book.publication_year
# Expected Output: ('1984', 'George Orwell', 1949)
```
