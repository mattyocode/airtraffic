class Airport():

    def __init__(self, location='TBC', capacity=5):
        self.location = location
        self.capacity = capacity
        self._terminals = []

    def add_plane_to_terminals(self, plane):
        if not self.is_full():
            self._terminals.append(plane)
        else:
            raise ValueError('Airport is full!')

    def remove_plane_from_terminals(self, plane):
        if plane in self._terminals:
            self._terminals.remove(plane)
        else:
            raise ValueError('Plane not at airport')

    def plane_in_terminals(self, plane):
        return plane in self._terminals

    def is_full(self):
        return len(self._terminals) >= self.capacity

    def empty_terminals(self):
        self._terminals = []