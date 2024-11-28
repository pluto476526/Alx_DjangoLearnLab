from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITest(TestCase):
    def setUp(self):
        # Create test client
        self.client = APIClient()

        # Create test users
        self.user = User.objects.create_user(username='user_john', password='12341234')
        self.staff_user = User.objects.create_superuser(username='admin_john', password='12341234')

        # Create test authors
        self.author1 = Author.objects.create(name='fake_auth')
        self.author2 = Author.objects.create(name='fake_auth2')

        # Create test books
        self.book1 = Book.objects.create(title='Fake book 1', author=self.author1, publication_year=1700)
        self.book2 = Book.objects.create(title='Fake book 2', author=self.author2, publication_year=2022)

        # Endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse('book-details', kwargs={'pk': pk})
        self.book_create_url = reverse('book-create')
        self.book_update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.book_delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

    # Test listing books
    def test_books_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test book details
    def test_book_details(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Fake book 1')

    # Test creating a book
    def test_create_book(self):
        fake_data = {'title': 'Fake book 3', 'author': self.author1.id, 'publication_year': 2013}

        # Unauthenticated user
        response = self.client.post(self.book_create_url, fake_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user
        self.client.login(username='admin_john', password='12341234')
        response = self.client.post(self.book_create_url, fake_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'Fake book 3')

    # Test updating a book
    def test_update_book(self):
        fake_data = {'title': 'Fake book updated', 'author': self.author1, 'publication_year': 1967}

        # Unauthenticated user
        response = self.client.put(self.book_update_url(self.book1.id), fake_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user
        self.client.login(username='admin_john', password='12341234')
        response = self.client.put(self.book_update_url(self.book1.id), fake_data)
        self.book1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book1.title, 'Fake book updated')

    # Test deleting a book
    def test_delete_book(self):
        # Unauthenticated user
        response = self.client.delete(self.book_delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user
        self.client.login(username='admin_john', password='12341234')
        response = self.client.delete(self.book_delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Test filtering books
    def test_filter_books(self):
        response = self.client.get(self.book_list_url + '?title=Fake book 2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2022)

    # Test searching books
    def test_search_books(self):
        response = self.client.get(self.book_list_url + '?search=Fake book 2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['name'], 'fake_auth2')

    # Test ordering books
    def test_order_books(self):
        response = self.client.get(self.book_list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Fake book 1')
