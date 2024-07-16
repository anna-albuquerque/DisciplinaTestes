import unittest

def factorial(n):
    #Implementação do método principal
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_positivo(self):
        #Implementação do teste
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)    

    def test_factorial_zero(self):
        #Implementação do teste
        self.assertEqual(factorial(0), 1)    

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            #Implementação do teste
            factorial(-1)        

if __name__ == '__main__':
    unittest.main()