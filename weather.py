import random

class Weather:
    '''A class to return weather condition \
        10% rainy / 90 % sunny'''

    def generate_random_number(self):
        return random.randint(1, 10)

    def check_state(self):
        '''Calls to set_state and returns \
            current state attribute'''
        n = self.generate_random_number()
        if n <=9:
            self.current_state = 'Sunny'
        else:
            self.current_state = 'Stormy'