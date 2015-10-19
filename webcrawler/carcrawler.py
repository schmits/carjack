import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carjack.settings")

import django
django.setup()

from bs4 import BeautifulSoup

import requests
from tidylib import tidy_document
from webcrawler.models import Brand


class CarCrawler:

    def __init__(self):
        pass


def main():
    response = requests.get('http://www.marktplaats.nl/c/auto-s/c91.html')
    print(response.status_code)
    tidy, errors = tidy_document(response.content)
    soup = BeautifulSoup(tidy)
    cars = soup.findAll('a', {'class' : 'car-brand'})
    print(cars)
    for car in cars:
        brand = Brand(None, car.string, car['href'])
        brand.name = car.string
        brand.url = car['href']
        print(brand.name)
        brand.save()

if __name__ == "__main__":
    main()