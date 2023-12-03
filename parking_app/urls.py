# parking_app/urls.py

from django.urls import path
from .views import register_user, main, reserved_places, static_page, reserve_place, skip_place, clear_place

urlpatterns = [
    path('', register_user, name='register_user'),
    path('main/', main, name='main'),
    path('reserved/', reserved_places, name='reserved_places'),
    path('Statistics/', static_page, name='static_page'),
    path('reserve/<int:place_id>/', reserve_place, name='reserve_place'),  # Add this line
    path('skip/', skip_place, name='skip_place'),  # Add this line
    #path('skip/<int:place_id>/', skip_place, name='skip_place'),

    path('clear_place/<int:place_id>/', clear_place, name='clear_place'),  # Add this line


    # Add more paths for other views
]
