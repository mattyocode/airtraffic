class Airport():
    '''A class to represent an airport'''

    def __init__(self, location='TBC', capacity=5):
        '''Initialises with location, capacity,  \
            and an empty terminal array'''
        self._location = location
        self._capacity = capacity
        self._terminals = []

    def get_location(self):
        '''Returns location'''
        return self._location

    def add_plane_to_terminals(self, plane):
        '''Adds plane instance to terminal \
            raises error if terminal at capacity'''
        if not self.is_full():
            self._terminals.append(plane)
        else: 
            raise ValueError('Airport is full!')

    def remove_plane_from_terminals(self, plane):
        '''Removes from terminal, \
            raises error if plane not in terminal'''
        if plane in self._terminals:
            self._terminals.remove(plane)
        else:
            raise ValueError('Plane not at airport')

    def plane_in_terminals(self, plane):
        '''Check if a plane instance in terminal'''
        return plane in self._terminals

    def is_full(self):
        '''Check if terminal is full'''
        return len(self._terminals) >= self._capacity

    def get_plane_list(self):
        '''View plane instances in terminal'''
        return [str(plane) for plane in self._terminals]

    def empty_terminals(self):
        '''Empty terminal of all plane instances'''
        self._terminals = []

