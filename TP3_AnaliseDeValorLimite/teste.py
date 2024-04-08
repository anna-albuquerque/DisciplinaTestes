import unittest
from modelo import Desconto

class DescontoTest(unittest.TestCase):
    # Idade e valor válido
    def test_IdadeEValorValido(self):
        valor = 250
        idade = 0
        compra = Desconto()
        self.assertTrue(compra._isElegivel(valor, idade))
        
        valor = 251
        idade = 1
        compra = Desconto()
        self.assertTrue(compra._isElegivel(valor, idade))

        valor = 251
        idade = 23
        compra = Desconto()
        self.assertTrue(compra._isElegivel(valor, idade))

        valor = 251
        idade = 24
        compra = Desconto()
        self.assertTrue(compra._isElegivel(valor, idade))


    # Idade e valor inválido
    def test_IdadeEValorInvalido(self):
        valor = 249
        idade = -1
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))

        valor = 249
        idade = 25
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))


    # Idade válida e valor inválido
    def test_IdadeValidaValorInvalido(self):
        valor = 249
        idade = 0
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))

        valor = 249
        idade = 1
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))
        
        valor = 249
        idade = 23
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))

        valor = 249
        idade = 24
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))


    # Idade inválida e valor válido
    def test_IdadeInvalidaValorValido(self):
        valor = 250
        idade = -1
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))

        valor = 251
        idade = -1
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))

        valor = 250
        idade = 25
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))

        valor = 251
        idade = 25
        compra = Desconto()
        self.assertFalse(compra._isElegivel(valor, idade))


    def test_ValidarDescontoIdadeMenorQue12Anos(self):
        # Valor com desconto = 212,5
        valor = 250
        idade = 0
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 212.5)

        valor = 250
        idade = 12
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 212.5)


    def test_ValidarDescontoIdadeMenorQue18Anos(self):
        # Valor com desconto = 220
        valor = 250
        idade = 13
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 220)

        valor = 250
        idade = 18
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 220)


    def test_ValidarDescontoIdadeMenorQue21Anos(self):
        # Valor com desconto = 237,5
        valor = 250
        idade = 19
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 237.5)

        valor = 250
        idade = 21
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 237.5)


    def test_ValidarDescontoIdadeMenorQue24Anos(self):
        # Valor com desconto = 242,5
        valor = 250
        idade = 22
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 242.5)

        valor = 250
        idade = 24
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertEqual(valor_com_desconto, 242.5)


    def test_DescontoNaoValidadoPelaIdade(self):
        valor = 250
        idade = 25
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertIsNone(valor_com_desconto)


    def test_DescontoNaoValidadoPeloValor(self):
        valor = 249
        idade = 24
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertIsNone(valor_com_desconto)

        valor = 249
        idade = 21
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertIsNone(valor_com_desconto)

        valor = 249
        idade = 18
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertIsNone(valor_com_desconto)

        valor = 249
        idade = 12
        compra = Desconto()
        valor_com_desconto = compra._validarDesconto(valor, idade)
        self.assertIsNone(valor_com_desconto)


if __name__ == "__main__":
    unittest.main()