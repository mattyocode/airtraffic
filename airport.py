class Airport():

    def __init__(self, id, capacity=5):
        self.id = id
        self.capacity = capacity
        self._terminals = []

    def plane_in_terminals(self, plane):
        return plane in self._terminals

