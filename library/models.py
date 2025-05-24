from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name  = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Book(models.Model):
    title  = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year   = models.PositiveIntegerField()

    @property
    def is_available(self) -> bool:
        return not hasattr(self, "loan")

    def __str__(self):
        return self.title


# ---------- POPRAWKA: *funkcja*, a nie lambda ----------
def default_due_date():
    """Zwraca datę zwrotu +30 dni od teraz."""
    return timezone.now() + timedelta(days=30)


class Loan(models.Model):
    book        = models.OneToOneField(Book, on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date    = models.DateTimeField(default=default_due_date)   # ← tu już bez lambda

    def __str__(self):
        return f"{self.book} → {self.user}"
