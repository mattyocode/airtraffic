class Airport():

    def __init__(self, id=1, capacity=5):
        self.id = id
        self.capacity = capacity
        self._terminals = []

    def plane_in_terminals(self, plane):
        return plane in self._terminals

    def is_full(self):
        return len(self._terminals) >= self.capacity

    def empty_terminals(self):
        self._terminals = []