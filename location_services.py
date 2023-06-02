import abc
import csv
import json
import requests

class LocationService(abc.ABC):
    @abc.abstractmethod
    def get_location(self, city, country):
        pass

class CSVLocationService(LocationService):
    def get_location(self, city, country):
        with open('worldcities.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == city and row[4] == country:
                    return float(row[2]), float(row[3])
        return None, None

class APILocationService(LocationService):
    def get_location(self, city, country):
        response = requests.get('https://nominatim.openstreetmap.org/search?q=' + city + ',' + country + '&format=json')
        location = json.loads(response.text)[0]
        return float(location['lat']), float(location['lon'])

class MockLocationService(LocationService):
    def get_location(self, city, country):
        return 12.9715987, 77.5945627