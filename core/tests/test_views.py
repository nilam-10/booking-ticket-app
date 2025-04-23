from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Show, Booking
from datetime import date, time

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')
        self.show = Show.objects.create(
            name='Test Show',
            date=date(2023, 12, 1),
            time=time(18, 0),
            venue='Test Venue',
            total_seats=100,
            available_seats=100
        )

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post_success(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass',
            'confirm_password': 'newpass'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_view_post_password_mismatch(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass',
            'confirm_password': 'wrongpass'
        })
        self.assertRedirects(response, reverse('register'))
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertRedirects(response, reverse('show_list'))

    def test_login_view_post_invalid(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertRedirects(response, reverse('login'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_show_list_view(self):
        response = self.client.get(reverse('show_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_list.html')
        self.assertContains(response, 'Test Show')

    def test_book_ticket_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('book_ticket', args=[self.show.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_ticket.html')

    def test_book_ticket_view_post_success(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('book_ticket', args=[self.show.id]), {
            'seats': 2
        })
        self.assertRedirects(response, reverse('booking_history'))
        self.assertEqual(Show.objects.get(id=self.show.id).available_seats, 98)
        self.assertTrue(Booking.objects.filter(user=self.user, show=self.show, seats=2).exists())

    def test_book_ticket_view_post_invalid_seats(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('book_ticket', args=[self.show.id]), {
            'seats': 101
        })
        self.assertRedirects(response, reverse('book_ticket', args=[self.show.id]))

    def test_booking_history_view(self):
        self.client.login(username='testuser', password='testpass')
        Booking.objects.create(user=self.user, show=self.show, seats=2)
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_history.html')
        self.assertContains(response, 'Test Show')

    def test_admin_dashboard_view_unauthorized(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 403)

    def test_admin_dashboard_view_authorized(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/dashboard.html')

    def test_manage_shows_view_add(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('manage_shows'), {
            'action': 'add',
            'name': 'New Show',
            'date': '2023-12-02',
            'time': '19:00',
            'venue': 'New Venue',
            'total_seats': 50
        })
        self.assertRedirects(response, reverse('manage_shows'))
        self.assertTrue(Show.objects.filter(name='New Show').exists())

    def test_view_bookings_view(self):
        self.client.login(username='admin', password='adminpass')
        Booking.objects.create(user=self.user, show=self.show, seats=2)
        response = self.client.get(reverse('view_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/view_bookings.html')
        self.assertContains(response, 'testuser')