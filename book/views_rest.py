from rest_framework import generics

from book.models import Book
from book.serializer import BookSerializer


class BookCreateRestView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookListRestView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
