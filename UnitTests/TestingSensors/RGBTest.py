import unittest
import busio
import adafruit_tcs34725
import time

class RGBTest(unittest.TestCase):
    def test_CreationTest(self):
        self.i2c = busio.I2C(1,0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        self.assertIsNotNone(self.sensor, "Le capteur a été créé avec succès.")
        self.assertIsNone(self.sensor, "Le capteur n'a pas été créé avec succès.")

    def test_ConnexionTest(self):
        self.i2c = busio.I2C(1, 0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        self.assertTrue(self.sensor.active, "Connexion établie")
        self.assertFalse(self.sensor.active, "Connexion non établie")

    def test_ReadColor(self):
        self.i2c = busio.I2C(1, 0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        if self.sensor.active:
            self.assertEqual(self.sensor.color_rgb_bytes[0], (200,255), "Couleur ROUGE détectée")
            self.assertEqual(self.sensor.color_rgb_bytes[1], (200,255), "Couleur VERT détectée")
            self.assertEqual(self.sensor.color_rgb_bytes[2], (200,255), "Couleur BLEU détectée")
            self.assertNotEqual(self.sensor.color_rgb_bytes[0], (200,255), "Couleur ROUGE non détectée")
            self.assertNotEqual(self.sensor.color_rgb_bytes[1], (200,255), "Couleur VERT non détectée")
            self.assertNotEqual(self.sensor.color_rgb_bytes[2], (200,255), "Couleur BLEU non détectée")

        else:
            print("Connexion non établie")

    def unti_test_values(self):
        self.i2c = busio.I2C(1, 0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        if self.sensor.active:
            value = self.sensor.read_value()
            self.assertIsInstance(value, int, "La valeur renvoyée est un entier")
            self.assertNotIsInstance(value, int, "La valeur renvoyée n'est pas un entier")

        else:
            print("Connexion non établie")

    def unit_test_NonUnderZeroValue(self):
        self.i2c = busio.I2C(1, 0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        if self.sensor.active:
            value = self.sensor.read_value()
            self.assertGreaterEqual(value, 0, "La valeur renvoyée est supérieure à 0")
            self.assertLess(value, 0, "La valeur renvoyée est inférieure à 0")

        else:
            print("Connexion non établie")
        
if __name__ == '__main__':
    unittest.main()