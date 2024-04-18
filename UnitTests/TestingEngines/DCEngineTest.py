import unittest
from Engines import DCEngine


class DCEngineTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def unit_test_exists(self):
        self.assertIsNotNone(self.engine)

    def unit_test_connection(self):
        self.assertTrue(self.pins.active)

    
    def unit_test_vitesse_negative(self):
        self.motor_state(self.motor1_A, self.motor1_B, -4095)
        self.motor_state(self.motor2_A, self.motor2_B, -4095)
        self.assertLess(pwm_value, 0, "La vitesse est négative")

    def unit_test_vitesse_positive(self):
        self.motor_state(self.motor1_A, self.motor1_B, 4095)
        self.motor_state(self.motor2_A, self.motor2_B, 4095)
        self.assertGreater(pwm_value, 0, "La vitesse est positive")

    def unit_test_vitesse_nulle(self):
        self.motor_state(self.motor1_A, self.motor1_B, 0)
        self.motor_state(self.motor2_A, self.motor2_B, 0)
        self.assertEqual(pwm_value, 0, "La vitesse est nulle")

if __name__ == '__main__':
    unittest.main()
