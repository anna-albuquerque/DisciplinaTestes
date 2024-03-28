import unittest
from triangulo import Triangulo


class TrianguloTest(unittest.TestCase):
    # Se é triângulo válido
    def test_ehTriangulo(self):
        a, b, c = 10, 15, 20
        t = Triangulo(a, b, c)
        self.assertTrue(t.validarForma())

    # Se triângulo não é válido
    def test_naoEhTriangulo(self):
        a, b, c = 10, 50, 20
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    # Se ângulos forem menor que zero
    def test_anguloMenorQueZero(self):
        a,b,c = -1, -2, 3
        with self.assertRaises(TypeError):
            t = Triangulo(a,b,c)


class TrianguloEquilateroTest(unittest.TestCase):
    def test_ehEquilatero(self):
        a, b, c = 10, 10, 10
        t = Triangulo(a,b,c)
        self.assertTrue(t.ehEquilatero)


    def test_naoEhEquilatero(self):
        # A != C
        a,b,c = 10, 10, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEquilatero())

        # A != B
        a,b,c = 15, 10, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEquilatero())

        # B != C
        a,b,c = 10, 10, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEquilatero())


        # Não ser triângulo
        a,b,c = 10, 50, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEquilatero())



class TrianguloIscolesTest(unittest.TestCase):
    def test_ehIsoceles(self):
        a,b,c = 10, 10, 15
        t = Triangulo(a,b,c)
        self.assertTrue(t.ehIsosceles())


    def test_naoEhIsoceles(self):
        # A = B e A = C
        a,b,c = 10, 10, 10
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehIsosceles())

        # A != B e B != C
        a,b,c = 10, 15, 20
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehIsosceles())

        # Não ser triangulo
        a,b,c = 10, 50, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEquilatero())


class TrianguloEscalenoTest(unittest.TestCase):
    def test_ehEscaleno(self):
        a,b,c = 10, 15, 20
        t = Triangulo(a,b,c)
        self.assertTrue(t.ehEscaleno)


    def test_naoEhEscaleno(self):
        # A = B e A != C
        a,b,c = 10, 10, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEscaleno())

        # A = C e A != B
        a,b,c = 10, 15, 10
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEscaleno())

        # B = C e A != B
        a,b,c = 15, 10, 10
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEscaleno())

        # A = B e A = C
        a,b,c = 10, 10, 10
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEscaleno())

        # Não ser triangulo
        a,b,c = 10, 50, 15
        t = Triangulo(a,b,c)
        self.assertFalse(t.ehEquilatero())


if __name__ == "__main__":
    unittest.main()