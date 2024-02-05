from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, UserFavoriteArticle


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.article = Article.objects.create(title='test title', content='test content', author=self.user)

    def test_favorites_view_for_logged_in_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('favorites'))
        self.assertEqual(response.status_code, 200)

    def test_favorites_view_for_logged_out_user(self):
        response = self.client.get(reverse('favorites'))
        self.assertNotEqual(response.status_code, 200)

    def test_publicatons_view_for_logged_in_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)

    def test_publicatons_view_for_logged_out_user(self):
        response = self.client.get(reverse('publications'))
        self.assertNotEqual(response.status_code, 200)

    def test_publish_view_for_logged_in_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)

    def test_publish_view_for_logged_out_user(self):
        response = self.client.get(reverse('publish'))
        self.assertNotEqual(response.status_code, 200)

    def test_new_user_creation_form_for_registered_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('register'))
        self.assertNotEqual(response.status_code, 200)

    def test_adding_same_article_twice_in_favorites(self):
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('article_detail', kwargs={'pk': self.article.pk}), {'article_id': self.article.id})
        self.client.post(reverse('article_detail', kwargs={'pk': self.article.pk}), {'article_id': self.article.id})
        favourite_count = UserFavoriteArticle.objects.filter(user=self.user, article=self.article).count()
        self.assertEqual(favourite_count, 1)