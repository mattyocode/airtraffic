from airport import Airport
from weather import Weather

class Plane():

    def __init__(self):
        self._status = None

    def set_to_land(self, airport, weather):
        if airport.is_full():
            raise ValueError('Airport is full!')
        elif:
            weather.check_state() == 'Stormy'
                raise ValueError('Weather is stormy')
        else:
            self._status = 'Landed'

    def set_to_takeoff(self):
        self._status = 'Flying'
    
    def clear(self):
        self._status = None

    
        