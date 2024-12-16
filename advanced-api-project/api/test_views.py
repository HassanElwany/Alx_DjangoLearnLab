from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author
import datetime


class BookAPITestCase(APITestCase):
    """Test case for the Book API endpoints."""

    def setUp(self):
        """Set up initial data for the tests."""
        self.author = Author.objects.create(name="Author 1")
        self.book1 = Book.objects.create(title="Book 1", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book 2", publication_year=2021, author=self.author)

        # Create a test user for authenticated tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.book_list_url = "/books/"
        self.book_detail_url = f"/books/{self.book1.id}/"

    def test_get_all_books(self):
        """Test retrieving all books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        """Test retrieving a single book."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """Test creating a new book."""
        data = {"title": "Book 3", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {"title": "Updated Book 1", "publication_year": 2019, "author": self.author.id}
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book 1")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by publication year."""
        response = self.client.get(f"{self.book_list_url}?publication_year=2021")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book 2")

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(f"{self.book_list_url}?search=Book 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book 1")

    def test_order_books(self):
        """Test ordering books by publication year."""
        response = self.client.get(f"{self.book_list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book 2")  # Newest book should come first

    def test_unauthenticated_user(self):
        """Test that unauthenticated users cannot create a book."""
        self.client.logout()
        data = {"title": "Unauthorized Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
