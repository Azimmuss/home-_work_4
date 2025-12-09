from django.db import models
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError("Ставьте оценку только от 1 до 5")


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")

    rating = models.IntegerField(validators=[validate_rating])

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if len(self.text) < 200:
            raise ValidationError("Текст отзыва должен быть минимум 200 символов")

    def __str__(self):
        return f"Review for {self.book.title}"
