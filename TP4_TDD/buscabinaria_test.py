import unittest

def busca_binaria(arr, x):
    #implementação do método principal
    primeiro = 0
    ultimo = len(arr) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if arr[meio] == x:
            return meio  
        elif arr[meio] < x:
            primeiro = meio + 1
        else:
            ultimo = meio - 1
    return -1  

class TestBuscaBinaria(unittest.TestCase):
    def test_encontrado(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(busca_binaria(arr, 7), 3)  

    def test_nao_encontrado(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(busca_binaria(arr, 8), -1)  
        
if __name__ == '__main__':
    unittest.main()