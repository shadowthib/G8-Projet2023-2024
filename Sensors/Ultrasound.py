from gpiozero import DistanceSensor
import lgpio
import time
class UltraSound:
    def __init__(self, echo, trigger, position):
        self.sensor = DistanceSensor(echo=echo, trigger=trigger)
        self.position = position

        @property
        def sensor(self):
            return self.sensor
        
        @property
        def position(self):
            return self.position
        
        @sensor.setter
        def sensor(self, sensor):
            if isinstance(sensor, DistanceSensor):
                self.sensor = sensor

        @position.setter
        def position(self, position):
            if isinstance(position, float):
                self.position = position

    def get_distance(self):
        while True:
            print("Distance (",self._position,") :")
            print(self._sensor.distance * 100)
            time.sleep(1)



'''while True:
    print(UltraSound_front.get_distance())
    time.sleep(0.1)'''