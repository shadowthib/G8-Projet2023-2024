import threading
import time
import PCA9685 as PCA
import Sensors.Ultrasound as UltraSound
import Engines.DCEngine as DCEngine
import Engines.ServoEngine as ServoEngine

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
        print("6: faire un demi tour")

        return input("Entrez votre choix : ")

    def demiTour(self):
            DC = DCEngine.DCEngine()
            SRV = ServoEngine.Servo()

            #DC.forward(1028)
            #time.sleep(5)

            angle = 20
            while angle < 65:
                SRV.set_angle(angle)
                time.sleep(0.1)
                angle += 1

            #time.sleep(2)
            SRV.set_angle(20)
            SRV.stop()
            #DC.stop()

menu = Main()

motor = DCEngine.DCEngine()
servo = ServoEngine.Servo()
UltraSound_front = UltraSound.UltraSound(5, 6, "Devant")
UltraSound_left = UltraSound.UltraSound(9, 11,"Gauche")
UltraSound_right = UltraSound.UltraSound(19,26,"Droite")

while 1:
    choix = menu.menu()
    if choix == "1":
        servo.bloquerRoueToutDroit()
        motor.avancerReculer30cm()
        servo.stop()
    elif choix == "2":
        motor.test_condition()
    elif choix == "3":
        servo.bloquerRoueToutDroit()
        motor.accelForward()
        motor.decelForward()
        servo.stop()
    elif choix == "4":
        servo.test()
    elif choix == "5":
        inp = input("Quel capteur voulez voir : [1] Devant [2] Gauche [3] Droite [4] Tous \n")
        if inp == "1":
            UltraSound_front.get_distance()
        elif inp == "2":
            UltraSound_left.get_distance()
        elif inp == "3":
            UltraSound_right.get_distance()
        elif inp == "4":
            UltraSound_front.get_distance()
            UltraSound_left.get_distance()
            UltraSound_right.get_distance()
        else :
            print("Recommencez votre choix")
        break
    elif choix == "6":
        motor.forward(2512,"R")
        servo.set_angle(65)
        time.sleep(3)
        motor.stop()
        motor.forward(2512,"L")
        servo.set_angle(-25)
        time.sleep(3)
        motor.stop()
        servo.set_angle(20)
        time.sleep(3)
        servo.stop()
        break
        # DC.stop()

    elif choix == "7":
        i = 0
        motor.avancer1M()
        while 1:
            if i == 0:
                motor.avancer1M()
            else :
                pass
            i += 1
            servo.mur1m(UltraSound_left.get_distance())

    elif choix == "8" :
        break
    else:
        print('Choix non valide, réessayer.')



