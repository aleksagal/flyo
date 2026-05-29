from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.flights_view, name='flights'),
    path('booking/<str:destination>/', views.booking_view, name='booking'),
]