import unittest
import RPi.GPIO as GPIO
import time

class UltrasoundTest(unittest.TestCase):

    def pin_unit_test(): # check s'il est bien coonecté sur le bon pin

    def type_unit_test(): #check si le type renvoyé est bien un float

    def distance_unit_test(): # ckeck si la distance renvoyé est bien comprise entre 0 et 400cm

    def stop_unit_test(): # arreter le moteur si la distence renvoyé est inférieurs à 2cm

    def tourner_unit_test(): # tourner et vérifier qu'il tourne s'il y moins de 10cm sur un capteur




if __name__ == '__main__':
    unittest.main()
