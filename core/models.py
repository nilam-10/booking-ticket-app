from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add this field

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add this field

    def __str__(self):
        return f"{self.user.username} - {self.show.name} - {self.seats} seats"