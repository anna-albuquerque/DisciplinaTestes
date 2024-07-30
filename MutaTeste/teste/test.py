import unittest
from main import Calculadora as c

class Test_calculadora(unittest.TestCase):
    def test_Soma(self):
        self.assertEqual(c.adicionar(1,1), 2)

    def test_Sub(self):
        self.assertEqual(c.subtrair(12,5), 7)
    
    def test_Multi(self):
        self.assertEqual(c.multiplicar(4,4), 16)

    def test_Div(self):
        self.assertEqual(c.dividir(12,5), 2.4)

""" if __name__ == '__main__':
    unittest.main() """ # Comentei para rodar o teste com o pytest, mas para excecutar com unittest (python test.py), descomente. 