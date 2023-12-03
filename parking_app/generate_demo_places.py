# parking_app/generate_demo_places.py

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from .models import ParkingPlace

class Command(BaseCommand):
    help = 'Generate demo parking places'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating demo places...'))

        # Create 150 places
        for i in range(1, 151):
            place_name = f"A-{i}"
            try:
                ParkingPlace.objects.create(name=place_name, is_available=True)
            except IntegrityError:
                # Handle the case where the place with the same name already exists
                pass

        self.stdout.write(self.style.SUCCESS('Demo places generated successfully!'))
