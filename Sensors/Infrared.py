from Sensor import Sensor

class InfraRed(Sensor):
    def __init__(self, bus_number):
        super().__init__(self)
        self.bus_number
        self.adress = 0x48

    def get_bus_number(self):
        return self.bus_number

    def get_adress(self):
        return self.adress

    def set_adress(self, adress):
        self.adress = adress
        self.notify()

    def set_bus_number(self, bus_number):
        self.bus_number = bus_number
        self.notify()

    def update(self):
        print(self.bus_number, self.adress, "updated")
        self.notify()
