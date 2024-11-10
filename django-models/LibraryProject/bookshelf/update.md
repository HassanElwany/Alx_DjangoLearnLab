```markdown
# Updating the title of the book to "Nineteen Eighty-Four"
```python
python manage.py shell

>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
# Expected Output: <Book: Nineteen Eighty-Four by George Orwell>
```
