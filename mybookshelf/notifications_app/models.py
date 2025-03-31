from django.db import models
from books_app.models import Book
from reading_plans_app.models import ReadingPlan



class Notification(models.Model):

    notification_type = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank= True, related_name='notifications')
    reading_plan = models.ForeignKey(ReadingPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='plan_notifications')
    message = models.TextField()
    is_read = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.notification_type} for {self.user.username} - {'Read' if self.is_read else 'Unread'}'