from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Show, Booking
from datetime import date, time

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.show = Show.objects.create(
            name='Test Show',
            date=date(2023, 12, 1),
            time=time(18, 0),
            venue='Test Venue',
            total_seats=100,
            available_seats=100
        )

    def test_show_str(self):
        self.assertEqual(str(self.show), 'Test Show - 2023-12-01')

    def test_booking_str(self):
        booking = Booking.objects.create(user=self.user, show=self.show, seats=2)
        self.assertEqual(str(booking), 'testuser - Test Show')