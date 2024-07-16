import unittest

class TestConta(unittest.TestCase):

    def test_criacao_conta_valores_corretos(self):
        conta = Conta(numero=1, agencia="001", saldo=100.0)
        self.assertEqual(conta.numero, 1)
        self.assertEqual(conta.agencia, "001")
        self.assertEqual(conta.saldo(), 100.0)

    def test_deposito(self):
        conta = Conta(numero=1, agencia="001", saldo=100.0)
        conta.depositar(50.0)
        self.assertEqual(conta.saldo(), 150.0)

    def test_saque_saldo_suficiente(self):
        conta = Conta(numero=1, agencia="001", saldo=100.0)
        conta.sacar(50.0)
        self.assertEqual(conta.saldo(), 50.0)

    def test_saque_saldo_insuficiente(self):
        conta = Conta(numero=1, agencia="001", saldo=100.0)
        with self.assertRaises(SaldoInsuficienteException):
            conta.sacar(150.0)

    def test_saldo_negativo(self):
        with self.assertRaises(ValueError):
            conta = lambda: Conta(numero=1, agencia="001", saldo=-100.0)
            conta()

class SaldoInsuficienteException(Exception):
    pass

class Conta:
    def __init__(self, numero, agencia, saldo):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.numero = numero
        self.agencia = agencia
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque.")
        self._saldo -= valor

    def saldo(self):
        return self._saldo

if __name__ == '__main__':
    unittest.main()
