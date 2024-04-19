from Sensor import Sensor
import time
from adafruit_circuitpython_tc77 import TC77

class InfraRed(S):
    def __init__(self):
        self.bus_number = 1
        self.adress = 0x40
        #self.threshold = threshold  # Seuil par défaut pour la détection de la ligne noire
        #self.is_on_black_line = False  # Indicateur de détection de la ligne noire
        self.sensorred = TC77(board.SCK, board.DIO)
        self.value = 0

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

    def line_mankou(self):
        while True:
            # Lire la valeur du capteur
            value = self.value

            # Vérifier si la ligne est détectée
            if value < 100:
                print("Ligne noire détectée!")
                motor.stop()
            else:
                print("Pas de ligne noire détectée.")

            # Attendre une seconde avant la prochaine lecture
            time.sleep(1)


def test():
    infra = InfraRed()

    infra.line_mankou()
    