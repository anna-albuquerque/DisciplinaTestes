import unittest
from unittest.mock import Mock
from datetime import time

class Sirene:
    def tocar(self):
        pass

class Relogio:
    def hora_atual(self):
        pass

class HorarioAulaOuIntervalo:
    def proximo_evento(self):
        pass

class GerenciadorSirene:
    def __init__(self, sirene: Sirene, relogio: Relogio, horario: HorarioAulaOuIntervalo):
        self.sirene = sirene
        self.relogio = relogio
        self.horario = horario

    def verificar_eventos(self):
        hora_atual = self.relogio.hora_atual()
        proximo_evento = self.horario.proximo_evento()
        if hora_atual == proximo_evento.hora:
            self.sirene.tocar()

class TestGerenciadorSirene(unittest.TestCase):

    def setUp(self):
        self.sirene = Mock()
        self.relogio = Mock()
        self.horario = Mock()
        self.gerenciador = GerenciadorSirene(self.sirene, self.relogio, self.horario)

    def test_tocar_sirene_no_horario_de_aula(self):
        horarios_aula = ["7:00", "7:45", "9:45", "10:30", "11:15", "12:00",
                         "13:00", "13:45", "14:30", "15:15", "17:15", "18:00"]

        for horario in horarios_aula:
            with self.subTest(horario=horario):
                self.relogio.hora_atual.return_value = horario
                self.horario.proximo_evento.return_value.hora = horario
                self.gerenciador.verificar_eventos()
                self.sirene.tocar.assert_called_once()
                self.sirene.tocar.reset_mock()  

    def test_tocar_sirene_no_intervalo(self):
        horarios_intervalo = ["8:30", "9:00", "16:00", "16:30"]

        for horario in horarios_intervalo:
            with self.subTest(horario=horario):
                self.relogio.hora_atual.return_value = horario
                self.horario.proximo_evento.return_value.hora = horario
                self.gerenciador.verificar_eventos()
                self.sirene.tocar.assert_called_once()
                self.sirene.tocar.reset_mock()  

    def test_nao_tocar_sirene_fora_de_horario_de_evento(self):
        horarios_fora_evento = ["6:00", "12:01", "18:01", "19:00"]

        for horario in horarios_fora_evento:
            with self.subTest(horario=horario):
                self.relogio.hora_atual.return_value = horario
                self.horario.proximo_evento.return_value.hora = "20:00" 
                self.sirene.tocar.assert_not_called()
                self.sirene.tocar.reset_mock()  

if __name__ == '__main__':
    unittest.main()