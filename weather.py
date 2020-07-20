import random

class Weather():
    '''A class to return weather condition'''
    
    def __init__(self):
        self.current_state = None

    def set_state(self):
        n = random.randint(1, 10)
        if n <=9:
            self.current_state = 'Sunny'
        else:
            self.current_state = 'Stormy'

    def check_state(self):
        self.set_state()
        return self.current_state