from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReadingPlanViewSet

router = DefaultRouter()
router.register(r'reading_plans', ReadingPlanViewSet)


urlpatterns =  [
    path('api/', include(router.urls)),
]