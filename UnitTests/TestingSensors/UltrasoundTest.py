import unittest
import RPi.GPIO as GPIO
import time

class UltrasoundTest(unittest.TestCase):

    def test_unit_sound (self):
        self.assertEqual(TRIG,1, "Le capteur a été activé")
        self.assertNotEqual(TRIG,1, "Le capteur n'a pas été activé")
        time.sleep(0.00001)
        self.assertEqual(ECHO,1, "Le capteur a pas activé")
        self.assertNotEqual(ECHO,1, "Le capteur n'a pas été activé")
        time.sleep(0.0011)
        self.assertEqual(TRIG,0, "Le capteur est activé")
        self.assertNotEqual(TRIG,0, "Le capteur est désactivé")
        self.assertEqual(ECHO,0, "Le capteur est activé")
        self.assertNotEqual(ECHO,0, "Le capteur est désactivé")

    def test_unit_distance(self):
        self.assertTrue(0<=distance<=400, "La distance est dans de la plage de mesure")
        self.assertFalse(0<=distance<=400, "La distance est hors de la plage de mesure")

    def test_unit_type(self):
        self.assertIsInstance(distance,float, "La distance est un nombre flottant")
        self.assertNotIsInstance(distance,float, "La distance n'est pas un nombre flottant")

    def test_unit_stop(self):
        self.assertTrue(distance>5, "La distance est supérieure à 5 cm")
        self.assertFalse(distance>5, "La distance est inférieure à 5 cm")

    def test_unit_start(self):
        self.assertTrue(distance<5, "La distance est inférieure à 5 cm")
        self.assertFalse(distance<5, "La distance est supérieure à 5 cm")

    
if __name__ == '__main__':
    unittest.main()