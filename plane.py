from airport import Airport
from weather import Weather

class Plane():

    def __init__(self):
        self._status = None

    def set_to_land(self, airport, weather):
        if airport.is_full():
            raise ValueError('Airport is full!')
        elif weather.check_state() == 'Stormy':
                raise ValueError('Weather is stormy')
        else:
            self._status = 'Landed'
            return self._status

    def set_to_takeoff(self, weather):
        if weather.check_state() == 'Stormy':
            raise ValueError('Weather is stormy')
        else:
            self._status = 'Flying'
            return self._status
    
    def clear(self):
        self._status = None

    
        