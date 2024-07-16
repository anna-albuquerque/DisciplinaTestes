import unittest

class Pilha:
    def __init__(self):
        self.items =[]
    
    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
class TestPilha(unittest.TestCase):

    def setUp(self):
        self.pilha = Pilha()

    def test_empilhar(self):
        #implementação do teste
        self.pilha.empilhar(1)
        self.pilha.empilhar(2)
        self.assertEqual(self.pilha.items, [1, 2])

    def test_desempilhar(self):
        #implementação do teste
        self.pilha.empilhar(1)
        self.pilha.empilhar(2)
        self.assertEqual(self.pilha.desempilhar(), 2)
        self.assertEqual(self.pilha.items, [1])

    def test_is_empty(self):
        #implementação do teste
        self.assertTrue(self.pilha.is_empty())
        self.pilha.empilhar(1)
        self.assertFalse(self.pilha.is_empty())

if __name__ == '__main__':
    unittest.main()