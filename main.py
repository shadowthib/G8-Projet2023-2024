import threading
import time
import Engines.DCEngine as DCEngine
import Sensors.Ultrasound as UltraSound
import Engines.ServoEngine as ServoEngine
import Sensors.Infrared as Infrared


import abc

class Main():
    def main(self):
        print("test")

    def menuPrincipal(self):
        while 1:
            choix = input("1: avancer/reculer 30cm\n2: gerer vitesse\n3: accelerer/decélération\n4: tourner servo\n5: récup donner ultraso\n6: demi tour\n7: longer mur\n8: faire un tour\n9: faire un tour aérodynamique\n10: YIONI-MENU (PERFORMANCE MAX)\n11: YIONITEST\nEntrez votre choix : ")
            match choix :
                case "1":
                    servo.bloquerRoueToutDroit()
                    motor.forward(1000)
                    time.sleep(2)
                    motor.stop()
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
                    time.sleep(3)
                    motor.stop()
                    servo.set_angle(20)
                    time.sleep(2)
                    servo.stop()
                    break
                case "7":
                    i = 0
                    while i <= 120:
                        distance = UltraSound_left.infiniteDistance()
                        distance_front = UltraSound_front.infiniteDistance()
                        servo.mur1m(distance)
                        #servo.mur1m(distance_front)
                        motor.forward(round(4095*0.35))
                        time.sleep(0.05)
                        i += 1
                    motor.stop()
                case "8":
                    nbrTour = input("Entrez le nombre de tour: ")
                    while True :
                        motor.forward(3000)
                        distance = UltraSound_left.infiniteDistance()
                        servo.mur1m(distance)
                        time.sleep(0.1)

                    motor.stop()
                    servo.set_angle(20)
                case "9":
                    servo.set_angle(-10)
                    time.sleep(2)

                    while True :
                        distance = UltraSound_left.infiniteDistance()
                        motor.forward(3000)
                        servo.collerMur(distance)
                        time.sleep(0.1)

                case "10":
                    y_choix = input("[1] YIONIMAX (Final) ")

                    match y_choix :
                        case "1":
                            infra = Infrared.InfraRed()
                            threading.Thread(target=infra.loopCount).start()

                            while not infra.loop_finished:
                                print("Moteur en marche")
                                distance_front = UltraSound_front.infiniteDistance()
                                distance_right = UltraSound_right.infiniteDistance()
                                distance_left = UltraSound_left.infiniteDistance()

                                threading.Thread(target=motor.Y_smartMove, args=(distance_front,distance_left,distance_right,)).start()
                                threading.Thread(target=servo.Y_smartFollowWall, args=(distance_left,distance_front,)).start()
                                threading.Thread(target=servo.smartTurn,
                                                 args=(distance_front, distance_left, distance_right,)).start()
                            motor.stop()
                            servo.stop()
                            print("C'est fini !")
                            '''while not infra.loop_finished:
                                print("pas fini")
                                distance_left = UltraSound_left.infiniteDistance()
                                distance_right = UltraSound_right.infiniteDistance()
                                distance_front = UltraSound_front.infiniteDistance()

                                threading.Thread(target=distance_left).start()
                                threading.Thread(target=distance_right).start()
                                threading.Thread(target=distance_front).start()


                                threading.Thread(target=motor.Y_smartMove, args=(distance_front,)).start()
                                threading.Thread(target=servo.Y_smartFollowWall, args=(distance_left,)).start()
                                #threading.Thread(target=servo.smartTurn, args=(distance_front,distance_left,distance_right,)).start()


                            else:
                                motor.stop()
                                servo.stop()'''

                            print(f"{threading.active_count()} Actifs !")
                            print(f"{threading.current_thread()}")


                            '''motor.smartMove(distance_front)
                            servo.smartFollowWall(distance_left)
                            servo.smartTurn(distance_front,distance_left,distance_right)'''
                case "11":
                    infra = Infrared.InfraRed()
                    #loop_finished = Infrared.InfraRed().loop_finished
                    threading.Thread(target=infra.loopCount).start()
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

