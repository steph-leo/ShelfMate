from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    model = Review
    field = '__all__'