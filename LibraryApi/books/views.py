
from rest_framework import generics

from .models import Book

from .serializers import BooksSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer



class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Book.objects.all()
    serializer_class = BooksSerializer