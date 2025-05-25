from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

def default_due_date():
    return timezone.now() + timedelta(days=14)

class Author(models.Model):
    name = models.CharField('Imię i nazwisko', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

class Book(models.Model):
    title = models.CharField('Tytuł', max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    year = models.PositiveIntegerField('Rok wydania')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book-detail', args=[self.pk])

    @property
    def is_available(self):
        return not self.loans.exists()  # zakładamy, że related_name='loans' w Loan

class Loan(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField('Termin zwrotu', default=default_due_date)  # domyślnie 14 dni do przodu

    class Meta:
        unique_together = ('user', 'book')
