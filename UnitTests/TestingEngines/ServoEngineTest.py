import unittest
import RPi.GPIO as GPIO
import time
import RPi as servo
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_pin(self):
        self.assertEqual(pin, 0)  # add assertion here
        
    
    def test_angle(self):
        #on définit une varaibla et lui donne 90
        cible_angle = 90
        #getposition permet de savoir la posivition du servo
        #position_actuelle = servo.get_position()
        servo.control_angle(cible_angle)
        position_finale = servo.get_position()
        self.assertEqual(position_finale, cible_angle)


        # Attention ton servo saura pas faire un 90° total avec les roues donc 180 pas possible
        self.assertEqual(angle_ligne,20)
        self.assertEqual(angle_gauche,-25)
        self.assertEqual(angle_droite,65)
        


    def test_in_range_true(self):
        self.sensor.get_angle=  lambda: 50
        self.assertTrue(self.sensor.in_range(-25,65),"le servo moteur tourne dans la range disponible")
        
        
        
    def test_in_range_false(self):
        self.sensor.get_angle=  lambda: -50
        self.assertFalse(self.sensor.is_in_range(-25,65), "le servo moteur tourne pas dans la range disponible")


    def test_erreur_communication(self):
        #simuler une erreur
        with mock.patch('servo.control_angle') as mock_control_angle:
            mock_control_angle.side_effect = OSError('Erreur de communication')
        #vérifier qu'une exception spécifique est levée pendant l'exécution du code à l'intérieur du bloc
        with self.assertRaises(OSError):
            cible_angle = 20
            servo.control_angle(cible_angle)
 
        # vérifier si la position est corecte par rapport àa ce qui a été demandé self.assertAlmostEqual(position_actuelle,cible_angle,delta=5)

        # vérifier si  l'angle est correcte par rapport à ce qui a été demandé self.assertIsNone(servo.control_angle(cible_angle))


        


if __name__ == '__main__':
    unittest.main()

    
