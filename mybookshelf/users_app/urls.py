from django.urls import path
from .views import RegisterUser, UserProfile, UpdateProfile

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    path('profile/update/', UpdateProfile.as_view(), name='update-profile'),
]
