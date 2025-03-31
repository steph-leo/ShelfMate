from django.db import models

from books_app.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews_app")
    reviewer = models.CharField(max_length=255)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.reviewer_name} - {self.book.title} ({self.rating}/5)'