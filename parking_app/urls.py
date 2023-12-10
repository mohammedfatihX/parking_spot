# parking_app/urls.py

from django.urls import path
from .views import register_user, main, reserved_places, static_page, reserve_place, clear_place ,main_skip 

urlpatterns = [
    path('', register_user, name='register_user'),
    path('main/', main, name='main'),
    path('reserved/', reserved_places, name='reserved_places'),
    path('Statistics/', static_page, name='static_page'),
    path('reserve/<int:place_id>/', reserve_place, name='reserve_place'),
    #path('skip/', skip_place, name='skip_place'), 
     path('skip/<int:place_id>/', main_skip, name='skip_place_id'),
    path('clear_place/<int:place_id>/', clear_place, name='clear_place'),


]
