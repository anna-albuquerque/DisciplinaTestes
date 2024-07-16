# Contrua uma função (em python) que realize o cálculo do desconto por dependente. A função
# recebe um valor, e a idade do dependente. A idade do dependente deve estar restrita ao intervalo [0..24]. 
# O valor mínimo da compra deve ser 250,00 reais. Para dependentes até 12 anos
# (inclusive) o desconto é de 15%. Entre 13 e 18 (inclusive) o desconto é de 12%. Dos 19 aos 21
# (inclusive) o desconto é de 5% e dos 22 aos 24 de 3%.

class Desconto:
    def __init__(self):
        self.valor = 0
        self.idade = 0
        self._desconto = 0

    def _isElegivel(self, valor:float, idade:int):
        if idade >= 0 and idade <= 24 and valor >= 250:
            return True
        return False

    def _calcularDesconto(self, idade):
        if idade <= 12:
            self._desconto = 0.15
        
        elif idade <= 18:
            self._desconto = 0.12

        elif idade <= 21:
            self._desconto = 0.05

        elif idade <= 24:
            self._desconto = 0.03

    def _validarDesconto(self, valor:float, idade:int):
        if self._isElegivel(valor, idade):
            self._calcularDesconto(idade)
            valor_com_desconto = valor * (1 - self._desconto)
            return valor_com_desconto