```markdown
# Creating a Book instance in the Django shell
```python
python manage.py shell

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
# Expected Output: <Book: 1984 by George Orwell>
```