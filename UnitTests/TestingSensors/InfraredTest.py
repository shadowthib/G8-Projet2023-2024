import unittest


class InfraredTest(unittest.TestCase):

    def unit_test_exists(self):
        self.assertIsNotNone(self.sensor, "Le capteur n'a pas été créé avec succès.")
        self.assertIsNone(self.sensor, "Le capteur à été créé avec succès.")  
    
    def unit_test_connection(self):
        self.assertTrue(self.sensor.active, "Connexion non établie")
        self.assertFalse(self.sensor.active, "Connexion établie")
    
    def unit_test_values(self):
        value = self.sensor.read_value()
        self.assertIsInstance(value, int, "La valeur renvoyée n'est pas un entier")
    
    def unit_test_NonUnderZeroValue(self):
        value = self.sensor.read_value()
        self.assertGreaterEqual(value, 0, "La valeur renvoyée est inférieure à 0")
        self.assertLess(value, 0, "La valeur renvoyée est supérieure à 0")

if __name__ == '__main__':
    unittest.main()
