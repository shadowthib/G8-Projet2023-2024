from gpiozero import DistanceSensor
import lgpio
import time
class UltraSound:
    def __init__(self, echo, trigger, position):
        self.sensor = DistanceSensor(echo=echo, trigger=trigger)
        self.position = position

    def get_distance(self):
        while True:
            print("Distance (",self.position,") :")
            print(self.sensor.distance * 100)
            time.sleep(0.1)
            return self.sensor.distance * 100

    def infiniteDistance(self):
        return round(self.sensor.distance * 100)





'''while True:
    print(UltraSound_front.get_distance())
    time.sleep(0.1)'''