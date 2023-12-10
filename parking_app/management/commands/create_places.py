# parking_app/management/commands/create_places.py

from django.core.management.base import BaseCommand
from parking_app.models import ParkingPlace


class Command(BaseCommand):
    help = 'Create 150 places in the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating 150 places...'))

        for i in range(1, 151):
            place_name = f"A-{i}"
            ParkingPlace.objects.create(name=place_name)

        self.stdout.write(self.style.SUCCESS('Places created successfully!'))
