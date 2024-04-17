import unittest
import RPi.GPIO as GPIO
import time

class UltrasoundTest(unittest.TestCase):

    def test_unit_sound (self):
        self.assertEqual(TRIG.value,1)
        time.sleep(0.00001)
        self.assertEqual(ECHO.value,1)
        time.sleep(0.0011)
        self.assertEqual(TRIG.value,0)
        self.assertEqual(ECHO.value,0)

    def test_unit_distance(self):
        self.assertTrue(0<=distance<=400)

    def test_unit_type(self):
        self.assertIsInstance(distance,float)

    def test_unit_stop(self):
        self.assertTrue(distance>5)
    
if __name__ == '__main__':
    unittest.main()
