from location_service_factory import LocationServiceFactory
from haversine import haversine

def get_distance(city1, country1, city2, country2, service_type):
    factory = LocationServiceFactory()
    service = factory.create(service_type)

    lat1, lon1 = service.get_location(city1, country1)
    lat2, lon2 = service.get_location(city2, country2)

    print(f'Latitud y longitud de {city1}, {country1}: {lat1}, {lon1}')
    print(f'Latitud y longitud de {city2}, {country2}: {lat2}, {lon2}')

    return haversine(lat1, lon1, lat2, lon2)


def main():
    ciudad1 = input('Ingrese la ciudad 1: ')
    pais1 = input('Ingrese el país 1: ')

    ciudad2 = input('Ingrese la ciudad 2: ')
    pais2 = input('Ingrese el país 2: ')

    tipo_servicio = input('Ingrese el tipo de servicio(CSV, API, Mock): ')
    print("Distancia:",get_distance(ciudad1, pais1, ciudad2, pais2, tipo_servicio))

    # Valores de prueba
    #print(get_distance('Lima', 'Peru', 'Buenos Aires', 'Argentina', 'CSV'))
    #print(get_distance('Lima', 'Peru', 'Buenos Aires', 'Argentina', 'API'))
    #print(get_distance('Lima', 'Peru', 'Buenos Aires', 'Argentina', 'Mock'))

main()