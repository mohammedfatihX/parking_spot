# parking_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import logging
from .models import ParkingPlace, User


def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        user = User.objects.create(name=name, phone_number=phone_number)
        request.session['user_id'] = user.id
        return redirect('main')

    return render(request, 'register_user.html')





def main(request):  
    available_place = ParkingPlace.objects.filter(is_available=True).first()
    return render(request, 'main.html', {'available_place': available_place})


def main_skip(request,place_id):
    place = get_object_or_404(ParkingPlace, id=place_id)
    if place.is_available:
        placeX = ParkingPlace.objects.filter(is_available=True,id__gt=place_id).order_by('id').first()
        return render(request, 'main.html', {'available_place': placeX})
 
    else:
        return render(request, 'place_not_available.html')

def reserved_places(request):
    # reserved_places = ParkingPlace.objects.filter(is_available=False)
    # non_reserved_places = ParkingPlace.objects.filter(is_available=True)
    allplace=ParkingPlace.objects.all()
    return render(request, 'reserved_places.html', {'places': allplace})


def static_page(request):
    total_places = ParkingPlace.objects.count()
    available_places = ParkingPlace.objects.filter(is_available=True).count()
    reserved_places = ParkingPlace.objects.filter(is_available=False).count()
    reserved_places_ = ParkingPlace.objects.filter(is_available=False)
    users = User.objects.all
    total_users = User.objects.count()

    return render(request, 'static_page.html', {
        'total_places': total_places,
        'available_places': available_places,
        'reserved_places': reserved_places,
        'total_users': total_users,
        "users":users
    })

def reserve_place(request, place_id):
    place = get_object_or_404(ParkingPlace, id=place_id)

    if place.is_available:
        place.is_available = False
        place.reserved_by_user = User.objects.get(id=request.session['user_id'])
        place.date_reserved = timezone.now()
        place.save()
        return redirect('reserved_places')
    else:
        return render(request, 'place_not_available.html')



def clear_place(request, place_id):
    place = get_object_or_404(ParkingPlace, id=place_id)

    if place.is_available:
        return render(request, 'place_already_available.html')

    place.is_available = True
    place.reserved_by_user = None
    place.date_reserved = None
    place.save()

    return redirect('reserved_places')


def deleteUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user:
        return render(request,'nouser.html')
    places =ParkingPlace.objects.filter(reserved_by_user=user.id).all()
    for place in places:
        place.is_available = True
        place.reserved_by_user = None
        place.date_reserved = None
        place.save()

    user.delete()
    return redirect('static_page')

    
    




