import random

class Weather():
    '''A class to return weather condition \
        10% rainy / 90 % sunny'''
    
    def __init__(self):
        '''Initialises with no state'''
        self.current_state = None

    def set_state(self):
        '''Returns random weather condition '''
        n = random.randint(1, 10)
        if n <=9:
            self.current_state = 'Sunny'
        else:
            self.current_state = 'Stormy'

    def check_state(self):
        '''Calls to set_state and returns \
            current state attribute'''
        self.set_state()
        return self.current_state

    def clear(self):
        '''Clears current state'''
        self.current_state = None