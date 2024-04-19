import threading
import time
import Engines.DCEngine as DCEngine
import Sensors.Ultrasound as UltraSound
import Engines.ServoEngine as ServoEngine


import abc

class Main():
    def main(self):
        print("test")

    def menuPrincipal(self):
        while 1:
            choix = input("1: avancer/reculer 30cm\n2: gerer vitesse\n3: accelerer/decélération\n4: tourner servo\n5: récup donner ultraso\n6: demi tour\n7: longer mur\nEntrez votre choix : ")
            match choix :
                case "1":
                    servo.bloquerRoueToutDroit()
                    motor.avancerReculer30cm()
                    servo.stop()
                case "2":
                    motor.test_condition()
                case "3":
                    servo.bloquerRoueToutDroit()
                    motor.accelForward()
                    motor.decelForward()
                    servo.stop()
                case "4":
                    servo.test()
                case "5":
                    self.menuUltrasond()
                case "6":
                    motor.forward(2512)
                    servo.set_angle(65)
                    time.sleep(3)
                    motor.stop()
                    motor.forward(2512)
                    servo.set_angle(-25)
                    time.sleep(3.5)
                    motor.stop()
                    servo.set_angle(20)
                    time.sleep(2)
                    servo.stop()
                    break
                case "7":
                    while True:
                        motor.avancer1M()
                        UltraSound_left.get_distance()
                        '''i = 0
                        while 1:
                            if i == 0:
                                motor.avancer1M()
                            else:
                                pass
                            i += 1
                            servo.mur1m(UltraSound_left.get_distance())'''
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

menu = Main()

motor = DCEngine.DCEngine()
servo = ServoEngine.Servo()
UltraSound_front = UltraSound.UltraSound(5, 6, "Devant")
UltraSound_left = UltraSound.UltraSound(9, 11,"Gauche")
UltraSound_right = UltraSound.UltraSound(19,26,"Droite")

menu.menuPrincipal()

