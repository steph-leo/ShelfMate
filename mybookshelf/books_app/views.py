from rest_framework import viewsets
from .models import Author, ReadingPlan, Book
from .serializers import AuthorSerializer, BookSerializer, ReadingPlanSerializer


class  AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class =AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReadingPlanViewSet(viewsets.ModelViewSet):
    queryset = ReadingPlan.objects.all()
    serializer_class = ReadingPlanSerializer
