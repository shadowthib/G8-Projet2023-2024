import unittest
import busio
import adafruit_tcs34725
import time

class TestTCS34725(unittest.TestCase):
    def test_CreationTest(self):
        self.i2c = busio.I2C(1,0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        self.assertIsNotNone(self.sensor, "Le capteur n'a pas été créé avec succès.")

    def test_ConnexionTest(self):
        self.i2c = busio.I2C(1, 0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        self.assertTrue(self.sensor.active)
        print("Connexion établie !")

    def test_ReadColor(self):
        self.i2c = busio.I2C(1, 0)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c, address=0x40)
        if self.sensor.active:
            self.assertEqual(self.sensor.color_rgb_bytes[0], (200,255), "Couleur ROUGE détectée")
            self.assertEqual(self.sensor.color_rgb_bytes[1], (200,255), "Couleur VERT détectée")
            self.assertEqual(self.sensor.color_rgb_bytes[2], (200,255), "Couleur BLEU détectée")
        else:
            print("Connexion non établie")

if __name__ == '__main__':
    unittest.main()

