import pytest
from django.urls import reverse
from .models import Author, Book

@pytest.mark.django_db
def test_create_book(client):
    author = Author.objects.create(first_name="Jan", last_name="Kowalski")
    response = client.post(reverse("library:book-add"), {
        "title": "Pan Tadeusz",
        "author": author.id,
        "year": 1834,
    }, follow=True)
    assert response.status_code == 200
    assert Book.objects.filter(title="Pan Tadeusz").exists()
