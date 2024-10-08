import random

class Dice:
    def __init__(self, size, negentropy_mode = False):
        self.size = size
        self.negentropy_mode = negentropy_mode

    def roll(self):
        if not self.negentropy_mode:
            return random.randint(1, self.size)
