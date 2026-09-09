# atv5

#EXERCÍCIO 1

import unittest

def calcular_desconto(valor_original: float, percentual_desconto: float) -> float:
    if not (0 <= percentual_desconto <= 100):
        ("O percentual de desconto deve estar entre 0 e 100.")
    
    desconto = valor_original * (percentual_desconto / 100)
    valor_final = valor_original - desconto
    
    return max(0.0, valor_final)

# --- TESTES ---
class TestCalcularDesconto(unittest.TestCase):
    def test_desconto_padrao(self):
        self.assertEqual(calcular_desconto(100.0, 10.0), 90.0)

    def test_percentual_invalido_maior_que_100(self):
        with self.assertRaises(ValueError):
            calcular_desconto(100.0, 150.0)

    def test_percentual_invalido_menor_que_zero(self):
        with self.assertRaises(ValueError):
            calcular_desconto(100.0, -10.0)

    def test_desconto_maior_que_valor_original(self):
        self.assertEqual(calcular_desconto(50.0, 100.0), 0.0)

if __name__ == "__main__":
    unittest.main()


#EXERCÍCIO 2
import unittest

def celsius_para_fahrenheit(celsius: float) -> float:
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError("Entrada deve ser um número válido.")
    
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)

def fahrenheit_para_celsius(fahrenheit: float) -> float:
    if not isinstance(fahrenheit, (int, float)) or isinstance(fahrenheit, bool):
        raise TypeError("Entrada deve ser um número válido.")
    
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)

# --- TESTES ---
class TestConversorTemperatura(unittest.TestCase):
    def test_celsius_para_fahrenheit_ponto_congelamento(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32.0)

    def test_celsius_para_fahrenheit_precisao(self):
        self.assertEqual(celsius_para_fahrenheit(37), 98.6)

    def test_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0.0)
        self.assertEqual(fahrenheit_para_celsius(100), 37.78)

    def test_entrada_nao_numerica(self):
        with self.assertRaises(TypeError):
            celsius_para_fahrenheit("37")
        with self.assertRaises(TypeError):
            fahrenheit_para_celsius(None)

if __name__ == "__main__":
    unittest.main()

#EXERCÍCIO 3
import unittest
import math

def calcular_valor_estacionamento(tempo_em_minutos: int) -> float:
    if tempo_em_minutos <= 0:
        raise ValueError("O tempo em minutos deve ser maior que zero.")
    
    if tempo_em_minutos <= 60:
        valor = 10.0
    else:
        horas_adicionais = math.ceil((tempo_em_minutos - 60) / 60)
        valor = 10.0 + (horas_adicionais * 5.0)
    
    return min(50.0, valor)

# --- TESTES ---
class TestEstacionamento(unittest.TestCase):
    def test_ate_primeira_hora(self):
        self.assertEqual(calcular_valor_estacionamento(45), 10.0)
        self.assertEqual(calcular_valor_estacionamento(60), 10.0)

    def test_hora_adicional_e_fracao(self):
        self.assertEqual(calcular_valor_estacionamento(70), 15.0)
        self.assertEqual(calcular_valor_estacionamento(120), 15.0)
        self.assertEqual(calcular_valor_estacionamento(121), 20.0)

    def test_teto_maximo_24h(self):
        self.assertEqual(calcular_valor_estacionamento(600), 50.0)

    def test_tempo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_valor_estacionamento(0)
        with self.assertRaises(ValueError):
            calcular_valor_estacionamento(-15)

if __name__ == "__main__":
    unittest.main()