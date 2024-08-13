class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2 

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return num1 / num2

calculadora = Calculadora()
print("Soma:", calculadora.somar(5, 3))
print("Subtração:", calculadora.subtrair(10, 4))
print("Multiplicação:", calculadora.multiplicar(6, 7))
print("Divisão:", calculadora.dividir(20, 4))