from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('flights/', views.flights_view, name='flights'),
    path('booking/<str:destination>/', views.booking_view, name='booking'),
    path('reserve/<int:flight_id>/', views.reserve_flight, name='reserve_flight'),
    path('reservations/', views.reservations, name='reservations'),
    path( "reservation/<int:reservation_id>/cancel/", views.cancel_reservation, name="cancel_reservation"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )