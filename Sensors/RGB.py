from Sensor import Sensor

class RGB(Sensor):
    def __init__(self):
        super().__init__(self)
        self.red = 0
        self.green = 0
        self.blue = 0
        

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.notify()

    def get_color(self):
        return self.red, self.green, self.blue
