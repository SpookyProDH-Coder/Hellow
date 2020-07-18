import random
from time import sleep

class happyBirthDay():
    def __init__(self):
        self.bpm = 80
    def pos(number):
        if number == 1:
            pos = 1
            return pos
        elif number == 2:
            pos = 2
            return pos
        elif number == 3:
            pos = 3
            return pos
        
        elif number == 4:
            pos = 4
            return pos

        elif number == "random":
            pos = random.randint(1, 4)
            return pos
