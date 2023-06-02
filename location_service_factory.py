from location_services import CSVLocationService, APILocationService, MockLocationService

class LocationServiceFactory:
    def create(self, type):
        if type == 'CSV':
            return CSVLocationService()
        elif type == 'API':
            return APILocationService()
        elif type == 'Mock':
            return MockLocationService()
