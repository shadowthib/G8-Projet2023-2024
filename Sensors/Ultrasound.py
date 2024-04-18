from gpiozero import DistanceSensor
import lgpio
import time
class UltraSound:
    def __init__(self, echo, trigger):
        self.sensor = DistanceSensor(echo=echo, trigger=trigger)

    def get_distance(self):
        return self.sensor.distance

UltraSound_front = UltraSound(5, 6)
UltraSound_left = UltraSound(9, 11)
UltraSound_right = UltraSound(19,26)

while True:
    print(UltraSound_front.get_distance())
    time.sleep(0.1)