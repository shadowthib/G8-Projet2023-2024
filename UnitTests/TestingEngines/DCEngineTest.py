from unittest.mock import patch
import unittest

class DCEngineTest(unittest.TestCase):
    def unit_test_exists(self):
        self.assertIsNotNone(self.DCEngine, "L'objet existe")

    def unit_test_connection(self):
        self.assertTrue(self.pins.active, "Les pins sont actives")

    def unit_test_vitesse(self):
        self.seepd_select = lambda: 512
        self.motor_state(self.motor1_A, self.motor1_B, self.speed_select)
        self.motor_state(self.motor2_A, self.motor2_B, self.speed_select)
        self.assertLess(self.seepd_select, 0, "La vitesse est négative")
        self.assertGreater(self.seepd_select, 0, "La vitesse est positive")
        self.assertEqual(self.seepd_select, 0, "La vitesse est nulle")

if __name__ == '__main__':
    unittest.main()
