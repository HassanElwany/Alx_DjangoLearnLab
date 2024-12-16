from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """Retrieve all books with filtering, searching, and ordering capabilities."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, searching, and ordering capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Specify fields for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Specify fields for search functionality
    search_fields = ['title', 'author__name']

    # Specify fields for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title

    def get_queryset(self):
        """Customize the queryset if additional logic is required."""
        queryset = super().get_queryset()
        # Add any dynamic filtering or adjustments to the queryset here if needed
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
