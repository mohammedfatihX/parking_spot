# parking_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

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
    reserved_places = ParkingPlace.objects.filter(is_available=False)
    non_reserved_places = ParkingPlace.objects.filter(is_available=True)
    return render(request, 'reserved_places.html', {'reserved_places': reserved_places,'availbe_places':non_reserved_places})


def static_page(request):
    total_places = ParkingPlace.objects.count()
    available_places = ParkingPlace.objects.filter(is_available=True).count()
    reserved_places = ParkingPlace.objects.filter(is_available=False).count()
    reserved_places_ = ParkingPlace.objects.filter(is_available=False)
    total_users = User.objects.count()

    return render(request, 'static_page.html', {
        'total_places': total_places,
        'available_places': available_places,
        'reserved_places_' : reserved_places_,
        'reserved_places': reserved_places,
        'total_users': total_users,
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

# def skip_place(request):
#     next_available_place = ParkingPlace.objects.filter(is_available=True).

#     if next_available_place:
#         return redirect('main_skip', place_id=next_available_place.id)
#     else:
#         return render(request, 'no_available_places.html')


def clear_place(request, place_id):
    place = get_object_or_404(ParkingPlace, id=place_id)

    if place.is_available:
        return render(request, 'place_already_available.html')

    place.is_available = True
    place.reserved_by_user = None
    place.date_reserved = None
    place.save()

    return redirect('reserved_places')

