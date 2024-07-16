import unittest

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        #Implementação do teste, verifica se a função converte corretamente
        self.assertEqual(convert_celsius_to_fahrenheit(0), 32)
        self.assertEqual(convert_celsius_to_fahrenheit(100), 212)
        self.assertEqual(convert_celsius_to_fahrenheit(-40), -40)
        self.assertEqual(convert_celsius_to_fahrenheit(37), 98.6)

def convert_celsius_to_fahrenheit(celsius):
    #implementação do método...
    return (celsius*9/5) + 32

if __name__ == '__main__':
    unittest.main()