import time

from RPi import GPIO

class InfraRed():
    def __init__(self):
        self.pin = 20
        self.loop_finished = False
        self.loop_track = -1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def lineDetect(self):
        return GPIO.input(self.pin)

    def loopCount(self):
        self.loop_finished = False
        loop_count = abs(int(input("Nombre de tour(s) à effectuer : ")))
        while not self.loop_finished:
            print("Détection ligne en cours...")
            if self.loop_track < loop_count:
                self.lineDetect()
                time.sleep(0.5)
                if self.lineDetect() == GPIO.HIGH:
                    print("Ligne détecté !")
                    self.loop_track += 1
                    time.sleep(2)
            elif self.loop_track >= loop_count:
                print("Tours terminés !")
                self.loop_finished = True
                return self.loop_finished
                break
