from django.test import TestCase
from .forms import BookForm
from .models import Author

class BookFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name="Jan Kowalski")

    def test_form_invalid_without_title(self):
        form = BookForm(data={
            'author': self.author.pk,
            'year': 2000
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_valid_with_all_fields(self):
        form = BookForm(data={
            'title': 'Ala ma kota',
            'author': self.author.pk,  # przekazujemy pk autora
            'year': 2000
        })
        self.assertTrue(form.is_valid())
