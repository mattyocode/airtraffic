from airport import Airport

class Plane():

    def __init__(self):
        self._status = None

    def set_to_land(self, airport):
        if airport.is_full():
            raise ValueError('Airport is full!')
        else:
            self._status = 'Landed'

    def set_to_takeoff(self):
        self._status = 'Flying'
    
    def clear(self):
        self._status = None

    
        