from rest_framework import serializers
from .models import Author, Book, ReadingPlan


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'

class ReadingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = '__all__'