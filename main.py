import threading
import time
import Engines.DCEngine as DCEngine
import Sensors.Infrared as InfraRed
import Sensors.Ultrasound as UltraSound
import Sensors.RGB as RGB


import abc

class Main():
    def main(self):
        infra = InfraRed()
        DC1 =  DCEngine(1, 2, 3)
        DC2 =  DCEngine(1, 2, 3)



    def menu(self):
        print("1: avancer/reculer 30cm")
        print("2: gerer accélération")
        print("3: accelerer/decélération")
        print("4: tourner servo")
        print("5: récup donner ultrason")
        print("6: ")

        return input("Entrez votre choix : ")

while 1:
    choix=menu()
    if choix=="1":
        avancerReculer30cm()
    elif choix=="2":
        test_condition()
    elif choix == "3":
        accelForward()
        decelForward()
    elif choix == "4":
        test()
    elif choix == "5":
        get_distcance()
    
   
        break
    else:
        print('Choix non valide, réessayer.')
