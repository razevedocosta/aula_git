import pytest
from calculadora import Calculadora

def test_somar():
    calculadora = Calculadora()
    assert calculadora.somar(5, 3) == 8

def test_subtrair():
    calculadora = Calculadora()
    assert calculadora.subtrair(10, 4) == 6

def test_multiplicar():
    calculadora = Calculadora()
    assert calculadora.multiplicar(6, 7) == 42

def test_dividir():
    calculadora = Calculadora()
    assert calculadora.dividir(20, 4) == 5
    assert calculadora.dividir(10, 0) == "Erro: Divisão por zero!"

if __name__ == "__main__":
    pytest.main()