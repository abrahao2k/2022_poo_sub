class Calculadora:
    valor1 = 0
    valor2 = 0
    
    def digitar(self):
        try:
            self.valor1 = int(input("Valor1? "))
            self.valor2 = int(input("Valor2? "))
            print("Valores armazenados no objeto.")
        except(TypeError, ValueError):
            print("Digite apenas números.")
    
    def somar(self):
        print(f"A soma é {self.valor1 + self.valor2}.")
    
    def dividir(self):
        try:
            print(f"A divisão é {self.valor1 / self.valor2}.")
        except ZeroDivisionError:
            print("Divisão por zero. Digite um valor diferente.")
    
    def imprimir(self):
        print(f"Valor1: {self.valor1}")
        print(f"Valor2: {self.valor2}")

'''
calc = Calculadora()
calc.digitar()
calc.somar()
calc.dividir()
calc.imprimir()
'''