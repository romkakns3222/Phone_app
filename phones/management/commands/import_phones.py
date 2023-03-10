import csv
import pathlib
from pathlib import Path


from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file = Path('venv', 'phones.csv')
        with open(file, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            id = phone['id']
            name = phone['name']
            image = phone['image']
            price = phone['price']
            release_date = phone['release_date']
            lte_exists = phone['lte_exists']
            Phone.objects.create(
                id=id,
                name=name,
                image=image,
                price=price,
                release_date=release_date,
                lte_exists=lte_exists,
            )

