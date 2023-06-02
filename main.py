import abc
import csv
import json
import requests
from math import radians, cos, sin, asin, sqrt

class LocationService(abc.ABC):
    @abc.abstractmethod
    def get_location(self, city, country):
        pass

class CSVLocationService(LocationService):
    def get_location(self, city, country):
        with open('worldcities.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == city and row[0] == country:
                    return float(row[3]), float(row[4])
        return None, None

class APILocationService(LocationService):
    def get_location(self, city, country):
        response = requests.get('https://nominatim.openstreetmap.org/search?q=' + city + ',' + country + '&format=json')
        location = json.loads(response.text)[0]
        return float(location['lat']), float(location['lon'])

class MockLocationService(LocationService):
    def get_location(self, city, country):
        return 12.9715987, 77.5945627  # Example fixed values

class LocationServiceFactory:
    def create(self, type):
        if type == 'CSV':
            return CSVLocationService()
        elif type == 'API':
            return APILocationService()
        elif type == 'Mock':
            return MockLocationService()

def haversine(lat1, lon1, lat2, lon2):
    r = 6371  # Radius of earth in kilometers
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)

    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    res = r * (2*asin(sqrt(a)))

    return res

def get_distance(city1, country1, city2, country2, service_type):
    factory = LocationServiceFactory()
    service = factory.create(service_type)

    lat1, lon1 = service.get_location(city1, country1)
    lat2, lon2 = service.get_location(city2, country2)

    return haversine(lat1, lon1, lat2, lon2)


print(get_distance('Lima', 'Peru', 'Buenos Aires', 'Argentina', 'API'))
