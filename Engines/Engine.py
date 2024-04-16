from abc import *
class Engine (metaclass=ABCMeta):
    def __init__(self, speed, pin):
        self.active = False
        self.speed = speed
        self.pin = pin
        self.dWheel = 0.065