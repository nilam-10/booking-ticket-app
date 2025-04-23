from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, ShowListView, BookTicketView,
    BookingHistoryView, AdminDashboardView, ManageShowsView, ViewBookingsView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', ShowListView.as_view(), name='show_list'),
    path('book/<int:show_id>/', BookTicketView.as_view(), name='book_ticket'),
    path('history/', BookingHistoryView.as_view(), name='booking_history'),
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/shows/', ManageShowsView.as_view(), name='manage_shows'),
    path('admin/bookings/', ViewBookingsView.as_view(), name='view_bookings'),
]