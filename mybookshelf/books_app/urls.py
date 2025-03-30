from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  AuthorViewSet, BookViewSet, ReadingPlanViewSet


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'plans', ReadingPlanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]