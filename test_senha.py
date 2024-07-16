import unittest
import re

def validar_senha(senha):
    if len(senha) < 8 or len(senha) > 20:
        return False
    if not re.search("[a-z]", senha):
        return False   
    if not re.search("[A-Z]", senha):
        return False
    if not re.search("[0-9]", senha):
        return False
    if not re.search("[!@#$%^&*]", senha):
        return False
    return True


class TestValidacaoSenha(unittest.TestCase):
    def test_senha_valida(self):
        self.assertTrue(validar_senha("Senha@123"))
    
    def test_senha_vazia(self):
        self.assertFalse(validar_senha(""))

    def test_senha_curta(self):
        self.assertFalse(validar_senha("Sen@1"))

    def test_senha_longa(self):
        self.assertFalse(validar_senha("Senha@123Senha@123Senha@123"))  

    def test_senha_sem_numero(self):
        self.assertFalse(validar_senha("Senha@Senha"))

    def test_senha_sem_caracter_especial(self):
        self.assertFalse(validar_senha("Senha123Senha"))

    def senha_sem_minuscula(self):
        self.assertFalse(validar_senha("SENHA@123"))

    def senha_sem_maiuscula(self):
        self.assertFalse(validar_senha("senha@123"))

if __name__ == '__main__':
    unittest.main()