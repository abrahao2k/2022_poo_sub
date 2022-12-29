class Pessoa2:
    __idade = 15
    __nome = "Carlos"
    
    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        if idade < 0 :
            idade = idade * -1
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def setNome(self,nome):
        self.__nome = nome
#########################################
p1 = Pessoa2()
p1.setNome("Xenófanes")
p1.setIdade(-21)
print(f"Me chamo {p1.getNome()} e tenho {p1.getIdade()} anos.")
