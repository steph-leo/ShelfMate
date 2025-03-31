from rest_framework import serializers
from .models import ReadingPlan

class ReadingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingPlan
        field = '__all__'