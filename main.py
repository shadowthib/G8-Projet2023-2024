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

    def menuPrincipal(self):
        while 1:
            choix = input("1: avancer/reculer 30cm\n2: gerer vitesse\n3: accelerer/decélération\n4: tourner servo\n5: récup donner ultraso\nEntrez votre choix : ")
            match choix :
                case "1":
                    motor.avancerReculer30cm()
                case "2":
                    motor.test_condition()
                case "3":
                    motor.accelForward()
                    motor.decelForward()
                case "4":
                    servo.test()
                case  "5":
                    self.menuUltrasond()                           
                case _: 
                    print('Choix non valide, réessayer.')
                    self.menuPrincipal()



    def menuUltrasond(self):
         while 1:
            inp = input("Quel capteur voulez voir :\n[0] Revenir en arriere\n[1] Devant\n[2] Gauche\n[3] Droite\n[4] Tous \nEntrez votre choix :")
            match inp :
                case "1":
                    UltraSound_front.get_distance()
                case "2":
                    UltraSound_left.get_distance()
                case "3":
                    UltraSound_right.get_distance()
                case "4":
                    UltraSound_front.get_distance()
                    UltraSound_left.get_distance()
                    UltraSound_right.get_distance()
                case "0":
                    break
                case _: 
                    print('Choix non valide, réessayer.')


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

menu.menuPrincipal()


