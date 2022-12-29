class Inimigo:
    def __init__(self):
        self.nome = "Malvadão"
        self.__vida = 10
    
    def verVida(self):
        print(self.__vida)
    
    def menosVida(self):
        self.__vida -= 2
        self.__morreu()
    
    def __morreu(self):
        if self.__vida <= 0:
            print("Morreu.")

#############################
in1 = Inimigo()
print(in1.nome)
for x in range(5):
    in1.verVida()
    in1.menosVida()


