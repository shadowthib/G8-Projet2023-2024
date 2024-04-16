from Sensor import Sensor
class UltraSound(Sensor):
    def __init__(self):
        super().__init__(self)
        self.distance = 0

    def set_distance(self, distance):
        self.distance = distance
        self.notify()

    def get_distance(self):
        return self.distance
