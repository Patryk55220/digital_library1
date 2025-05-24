from django.test import TestCase
from .models import Book, Author

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # najpierw autor
        cls.author = Author.objects.create(name="Autor Testowy")
        # potem książka
        cls.book = Book.objects.create(
            title="Tytuł", 
            author=cls.author, 
            year=2020
        )

    def test_str(self):
        self.assertEqual(str(self.book), "Tytuł")

    def test_get_absolute_url(self):
        url = self.book.get_absolute_url()
        # zakładam, że URL to /book/<pk>/
        self.assertTrue(url.endswith(f"/book/{self.book.pk}/"))
