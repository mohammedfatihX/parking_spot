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


# views.py



def main(request):
    # Retrieve the first available place from the database
    available_place = ParkingPlace.objects.filter(is_available=True).first()
    return render(request, 'main.html', {'available_place': available_place})

def reserved_places(request):
    reserved_places = ParkingPlace.objects.filter(is_available=False)
    return render(request, 'reserved_places.html', {'reserved_places': reserved_places})


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
    # Get the ParkingPlace object by place_id
    place = get_object_or_404(ParkingPlace, id=place_id)

    # Check if the place is available
    if place.is_available:
        # Mark the place as reserved
        place.is_available = False

        # Assign the user who reserved the place (replace this with your authentication logic)
        #user_id =


        # Handle the case where the user is not authenticated
        #user = User.objects.first()  # Assuming there is at least one user
        place.reserved_by_user = User.objects.get(id=request.session['user_id'])

        # Set the date when the place was reserved using timezone.now()
        place.date_reserved = timezone.now()

        # Save the changes to the database
        place.save()

        # Redirect to the main page or any other page as needed
        return redirect('main')
    else:
        # Handle the case where the place is not available (optional)
        return render(request, 'place_not_available.html')

def skip_place(request):
    # Get the next available parking place
    next_available_place = ParkingPlace.objects.filter(is_available=True).first()

    if next_available_place:
        # Redirect to the reservation page for the next available place
        return redirect('reserve_place', place_id=next_available_place.id)
    else:
        # Handle the case when there are no available places (optional)
        return render(request, 'no_available_places.html')


def clear_place(request, place_id):
    # Get the ParkingPlace object by place_id
    place = get_object_or_404(ParkingPlace, id=place_id)

    # Check if the place is reserved
    if place.is_available:
        # Handle the case where the place is already available (optional)
        return render(request, 'place_already_available.html')

    # Clear the place (mark it as available and remove reservation details)
    place.is_available = True
    place.reserved_by_user = None
    place.date_reserved = None
    place.save()

    # Redirect to the reserved places page or any other page as needed
    return redirect('reserved_places')

