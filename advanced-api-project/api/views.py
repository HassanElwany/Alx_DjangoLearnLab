from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """Retrieve all books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        """Filter books based on query parameters (if needed)"""
        queryset = super().get_queryset()
        # Example: Uncomment to filter books by current year
        # current_year = datetime.datetime.now().year
        # return queryset.filter(publication_year=current_year)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    """Retrieve details of a single book by ID"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    """Create a new book (restricted to authenticated users)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Customize create logic if needed"""
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book (restricted to authenticated users)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """Customize update logic if needed"""
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """Delete an existing book (restricted to authenticated users)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
