from django.urls import path

from .views import NotificationList,  NotificationDetail, MarkNotificationAsRead

urlpattern = [
    path('notifications/', NotificationList.as_view(), name = ' notification-list'),
    path('notifications/<int:pk>/', NotificationDetail.as_view(), name = 'notification-detail'),
    path('notifications/<int:pk>/read/', MarkNotificationAsRead.as_view(), name = "mark-notification-read")
]