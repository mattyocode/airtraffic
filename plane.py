from airport import Airport
from weather import Weather

class Plane():
    '''A class to represent a plane'''

    def __init__(self, id_num="Not set"):
        '''Initialises with id number, status \
            and location set to none'''
        self._id_num = id_num
        self._status = None
        self._current_location = None

    def __str__(self):
        '''Returns id number for plane instance'''
        return f"{self._id_num}"

    def can_land(self, airport, weather):
        '''Checks that plane is flying, weather is \
            sunnyu and there is free terminal space \
            to allow plane to land'''
        if self._status == 'Flying':
            raise ValueError('Already landed!')
        elif airport.is_full():
            raise ValueError('Airport is full!')
        elif weather.check_state() == 'Stormy':
            raise ValueError('Weather is stormy')
        else:
            return True

    def set_to_land(self, airport, weather):
        '''Tells plane to land, adds it to terminal, \
            sets status to landed, updates plane \
            location'''
        if self.can_land(airport, weather):
            airport.add_plane_to_terminals(self)
            self._status = 'Landed'
            self._current_location = airport.get_location()
            return self._status

    def can_takeoff(self, airport, weather):
        '''Checks if weather is stormy, the plane is \
            in the correct airport, and isn't already \
                flying before take off'''
        if weather.check_state() == 'Stormy':
            raise ValueError('Weather is stormy')
        elif airport.get_location() != self._current_location:
            raise ValueError('Wrong airport')
        elif self._status == 'Flying':
            raise ValueError('Plane is in flight!')
        else:
            return True

    def set_to_takeoff(self, airport, weather):
        '''Removes plane from airport terminal \
            sets status to flying, removes location \
            data, returns current status'''
        if self.can_takeoff(airport, weather):
            airport.remove_plane_from_terminals(self)
            self._status = 'Flying'
            self._current_location = None
            return self._status

    def current_location(self):
        '''Returns current location attribute'''
        return f'{self._current_location}'
    
    def clear(self):
        '''Sets status to None'''
        self._status = None

    
        