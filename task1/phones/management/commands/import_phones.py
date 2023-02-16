import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug = phone['name'].replace(' ','_').lower()
            if Phone.objects.filter(slug = slug):
                slug = slug + f'({phone["id"]})'
            
            db = Phone(
                id = phone['id'], 
                name = phone['name'],
                price = phone['price'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists'],
                image = phone['image'],
                slug = slug
            )
            db.save()
            pass
