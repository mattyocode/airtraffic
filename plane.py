class Plane():

    def __init__(self):
        self._status = None

    def set_to_land(self):
        self._status = 'Landed'

    def set_to_takeoff(self):
        self._status = 'Flying'