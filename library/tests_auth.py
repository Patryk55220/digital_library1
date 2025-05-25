# library/tests_auth.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='pass')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('library:profile'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/profile/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.get(reverse('library:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/profile.html')
