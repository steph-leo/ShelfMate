from django.db import models

from books_app.models import Book

class ReadingPlan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reading_plans_reading_plans_app")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_days = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        '''calculate days dynamical before saving'''
        if self.start_date and self.end_date:
            self.total_days = (self.end_date - self.start_date).days
        super().save(*args, **kwargs)

    def __str__(self):
        return f'plan for {self.book.title} ({self.start_date}-{self.end_date})'
