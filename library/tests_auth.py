from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class ProfileViewTest(TestCase):
    def setUp(self):
        # tworzymy użytkownika
        self.user = User.objects.create_user(username='użytkownik', password='tajne')

    def test_redirect_if_anonymous(self):
        url = reverse('library:profile')
        resp = self.client.get(url)
        # powinno przekierować na login i dopisać next=
        self.assertRedirects(resp, f"{reverse('login')}?next={url}")

    def test_profile_for_logged_in(self):
        self.client.login(username='użytkownik', password='tajne')
        resp = self.client.get(reverse('library:profile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/profile.html')
