from airport import Airport
from weather import Weather

class Plane():

    def __init__(self, id_num="Not set"):
        self._id_num = id_num
        self._status = None
        self._current_location = None

    def can_land(self, airport, weather):
        if airport.is_full():
            raise ValueError('Airport is full!')
        elif weather.check_state() == 'Stormy':
            raise ValueError('Weather is stormy')
        else:
            return True

    def set_to_land(self, airport, weather):
        if self.can_land(airport, weather):
            airport.add_plane_to_terminals(self)
            self._status = 'Landed'
            self._current_location = airport.get_location()
            return self._status

    def can_takeoff(self, airport, weather):
        if weather.check_state() == 'Stormy':
            raise ValueError('Weather is stormy')
        elif airport.get_location() != self._current_location:
            raise ValueError('Wrong airport')
        elif self._status == 'Flying':
            raise ValueError('Plane is in flight!')
        else:
            return True

    def set_to_takeoff(self, airport, weather):
        if self.can_takeoff(airport, weather):
            airport.remove_plane_from_terminals(self)
            self._status = 'Flying'
            return self._status

    def current_location(self):
        return self._current_location
    
    def clear(self):
        self._status = None

    
        