class Pessoa:
    nome  = ""
    idade = ""
    
    def __init__(self, pnome, pidade):
        self.nome = pnome
        self.idade = pidade
######################################
    
#p1 = Pessoa() # dá erro

p1 = Pessoa("Camila", 26)
p2 = Pessoa("Kaio", 19)

nome3 = input("Digite o nome: ")
idade3 = input("Digite a idade: ")
p3 = Pessoa(nome3, idade3)

print(f"{p1.nome} tem {p1.idade} anos.")
