import threading
import time
import Engines.DCEngine as DCEngine
import Sensors.Infrared as InfraRed
import Engines.ServoEngine as Servo
import Sensors.Ultrasound as UltraSound
import Sensors.RGB as RGB

import abc


class Main():
    def main(self):
        print("test")

    def menu(self):
        print("1: avancer/reculer 30cm")
        print("2: gerer vitesse")
        print("3: accelerer/decélération")
        print("4: tourner servo")
        print("5: récup donner ultrason")

        return input("Entrez votre choix : ")


motor = DCEngine.DCEngine()
servo = Servo.Servo()
ultra = UltraSound.UltraSound(5, 6)

while 1:
    choix = Main()
    if choix == "1":
        motor.avancerReculer30cm()
    elif choix == "2":
        motor.test_condition()
    elif choix == "3":
        motor.accelForward()
        motor.decelForward()
    elif choix == "4":
        servo.test()
    elif choix == "5":
        ultra.get_distance()

        break
    else:
        print('Choix non valide, réessayer.')


menu = Main()
menu.menu()