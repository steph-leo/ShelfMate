from rest_framework import viewsets
from .models import ReadingPlan
from .serializers import ReadingPlanSerializer

class ReadingPlanViewSet(viewsets.ModelViewSet):
    queryset = ReadingPlan.objects.all()
    serializer_class = ReadingPlanSerializer
