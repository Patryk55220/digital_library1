from django.db import models
from django.contrib.auth import get_user_model

class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    class Meta:
        unique_together = ("first_name", "last_name")
        ordering = ("last_name",)
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    year = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ("title",)
    def __str__(self):
        return self.title
    @property
    def is_available(self):
        return not hasattr(self, "loan")

class Loan(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    def __str__(self):
        return f"{self.book} → {self.user}"
