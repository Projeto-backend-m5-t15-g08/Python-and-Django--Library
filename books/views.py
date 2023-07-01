from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from books.models import Book
from books.serializer import BookSerializer


class BookView(CreateAPIView):
    queryset: Book.objects.all()
    serializer_class = BookSerializer
