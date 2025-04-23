from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Show, Booking

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('show_list')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('login')

class ShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'show_list.html', {'shows': shows})

class BookTicketView(View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'book_ticket.html', {'show': show})

    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        seats = request.POST.get('seats')

        try:
            seats = int(seats)
            if seats <= 0 or seats > show.available_seats:
                messages.error(request, "Invalid seat selection")
                return redirect('book_ticket', show_id=show_id)

            total_cost = show.ticket_price * seats
            Booking.objects.create(user=request.user, show=show, seats=seats, total_cost=total_cost)
            show.available_seats -= seats
            show.save()
            messages.success(request, "Booking confirmed")
            return redirect('booking_history')
        except ValueError:
            messages.error(request, "Please enter a valid number of seats")
            return redirect('book_ticket', show_id=show_id)

class BookingHistoryView(View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'booking_history.html', {'bookings': bookings})

class AdminDashboardView(View):
    def get(self, request):
        if not request.user.is_staff:
            return HttpResponse("Unauthorized", status=403)
        return render(request, 'admin/dashboard.html')

class ManageShowsView(View):
    def get(self, request):
        if not request.user.is_staff:
            return HttpResponse("Unauthorized", status=403)
        shows = Show.objects.all()
        return render(request, 'admin/manage_shows.html', {'shows': shows})

    def post(self, request):
        if not request.user.is_staff:
            return HttpResponse("Unauthorized", status=403)

        action = request.POST.get('action')
        if action == 'add':
            name = request.POST.get('name')
            date = request.POST.get('date')
            time = request.POST.get('time')
            venue = request.POST.get('venue')
            total_seats = request.POST.get('total_seats')
            ticket_price = request.POST.get('ticket_price')

            try:
                total_seats = int(total_seats)
                ticket_price = float(ticket_price)
                Show.objects.create(
                    name=name,
                    date=date,
                    time=time,
                    venue=venue,
                    total_seats=total_seats,
                    available_seats=total_seats,
                    ticket_price=ticket_price
                )
                messages.success(request, "Show added successfully")
            except ValueError:
                messages.error(request, "Invalid input for seats or ticket price")
        elif action == 'edit':
            show_id = request.POST.get('show_id')
            show = get_object_or_404(Show, id=show_id)
            show.name = request.POST.get('name')
            show.date = request.POST.get('date')
            show.time = request.POST.get('time')
            show.venue = request.POST.get('venue')
            show.total_seats = int(request.POST.get('total_seats'))
            show.available_seats = int(request.POST.get('available_seats'))
            show.ticket_price = float(request.POST.get('ticket_price'))
            show.save()
            messages.success(request, "Show updated successfully")
        elif action == 'delete':
            show_id = request.POST.get('show_id')
            show = get_object_or_404(Show, id=show_id)
            show.delete()
            messages.success(request, "Show deleted successfully")

        return redirect('manage_shows')

class ViewBookingsView(View):
    def get(self, request):
        if not request.user.is_staff:
            return HttpResponse("Unauthorized", status=403)
        bookings = Booking.objects.all()
        return render(request, 'admin/view_bookings.html', {'bookings': bookings})
