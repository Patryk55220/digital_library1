from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Author, Book


class BookViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name="Y")
        Book.objects.create(title="X", author=cls.author, year=1999)
        # Tworzymy usera do logowania
        cls.user = User.objects.create_user(username='testuser', password='12345')

    def setUp(self):
        # Logujemy się przed każdym testem
        self.client.login(username='testuser', password='12345')

    def test_list_view(self):
        resp = self.client.get(reverse('library:book-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/book_list.html')

    def test_detail_view(self):
        book = Book.objects.first()
        resp = self.client.get(reverse('library:book-detail', args=[book.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, book.title)

    def test_create_redirects(self):
        author = Author.objects.create(name="Z")
        resp = self.client.post(reverse('library:book-add'), {
            'title': 'Nowa książka',
            'author': author.pk,
            'year': 2025
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Book.objects.filter(title='Nowa książka').exists())
