from Engine import Engine
import time
from main import Main

class DCEngine(Engine):
    def __init__(self, time, speed, pin):
        super().__init__(speed, pin)
        self.time = time

def setSpeed(self, speed):
    self.speed = speed

def setAngle(self):
    while self.running == True:
        self.angle += 1
