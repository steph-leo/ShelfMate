from django.urls import path, include
from .views import ReviewListCreate,  ReviewDetail


urlpatterns = [
    path('review/', ReviewListCreate.as_view(), name = 'review-list-create'),
    path('reviews/<int:pk', ReviewDetail.as_view(), name = 'review-detail'),
]