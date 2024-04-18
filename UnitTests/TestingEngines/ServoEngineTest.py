import unittest
import RPi.GPIO as GPIO
import time
import RPi.Servo as servo
import Adafruit_Servo as servo


class MyTestCase(unittest.TestCase):
    def test_pin(self):
        self.assertEqual(pin_trigger, 18)  # add assertion here
        self.assertEqual(pin_echo, 24)
        self.assertEqual(pin_moteur, 27)
    
    def test_angle(self):
        #on définit une varaibla et lui donne 90
        cible_angle = 90
        #getposition permet de savoir la posivition du servo
        position_actuelle = servo.get_position()
        servo.control_angle(cible_angle)
        position_finale = servo.get_position()
        self.assertEqual(position_finale, cible_angle)


        # Attention ton servo saura pas faire un 90° total avec les roues donc 180 pas possible
        self.assertEqual(angle_ligne,90)
        self.assertEqual(angle_gauche,50)
        self.assertEqual(angle_droite,130)
        


    def test_in_range_true(self):
        self.sensor.get_angle=  lambda: 50
        self.assertTrue(self.sensor.in_range(0,180),"le servo moteur tourne dans la range disponible")
        
        
        
    def test_in_range_false(self):
        self.sensor.get_angle=  lambda: -50
        self.assertFalse(self.sensor.is_in_range(0, 180), "le servo moteur tourne pas dans la range disponible")

    
"""""
 def testgetdistance_returns_float(self):
        self.sensor.get_distance = lambda: 25.5
        distance = self.sensor.get_distance()
        self.assertIsInstance(distance, float, "La distance doit être un float")

    def test_is_in_range_true(self):
        self.sensor.get_distance = lambda: 25.5
        self.assertTrue(self.sensor.is_in_range(20, 30), "Le capteur devrait détecter l'objet dans la plage")

    def test_is_in_range_false_outside_max(self):
        self.sensor.get_distance = lambda: 35.5
        self.assertFalse(self.sensor.is_in_range(20, 30), "L'objet est hors de la plage maximale")

    def test_is_in_range_false_inside_min(self):
        self.sensor.get_distance = lambda: 15.5
        self.assertFalse(self.sensor.is_in_range(20, 30), "L'objet est en dessous de la plage minimale")

    def test_get_distance_none_when_error(self):
        # Simule un scénario où le capteur ne peut pas lire la distance
        self.sensor.get_distance = lambda: None
        distance = self.sensor.get_distance()
        self.assertIsNone(distance, "La fonction doit retourner None en cas d'erreur de lecture")

    def test_distance_in_expected_range(self):
        self.sensor.get_distance = lambda: 22.5
        distance = self.sensor.get_distance()
        self.assertIn(distance, range(20, 31), "La distance doit être dans la plage attendue")

    def test_distance_not_equal_unexpected_value(self):
        self.sensor.get_distance = lambda: 22.5
        distance = self.sensor.get_distance()
        self.assertNotEqual(distance, 50.0, "La distance ne doit pas être égale à une valeur inattendue")
"""""

        
        """
        pas de if car c'est pas un test unitaire
        if cible_angle== 90:
            print("je vais tout droit")

        if cible_angle== 0:
            print("je vais à  l'extreme gauche")

        if cible_angle==180:
            print("je vais à l'extreme droite")"""

        # vérifier si la position est corecte par rapport àa ce qui a été demandé self.assertAlmostEqual(position_actuelle,cible_angle,delta=5)

        # vérifier si  l'angle est correcte par rapport à ce qui a été demandé self.assertIsNone(servo.control_angle(cible_angle))


        #si la voiture doit aller tout droit  
        #alors l'angle doit etre à ...
        #self.assertEqual(angle_ligne,90)
        #si la voiture doit tourner à gauche
        #alors l'angle doit etre à ...
        #self.assertEqual(angle_gauche,45)
        #si la voiture doit tourner à droite
        #alors l'angle doit etre à ...
        #self.assertEqual(angle_droite,180)


if __name__ == '__main__':
    unittest.main()

    
