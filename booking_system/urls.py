from django.urls import path
from . import views

app_name = 'booking_system'

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]
