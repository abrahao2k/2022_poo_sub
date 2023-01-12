from classePessoa import Pessoa

class Professor(Pessoa):
    __salario = None
    __formacao = None
    
    def __init__(self, nome, idade, salario, formacao):
        super().__init__(nome, idade)
        self.__salario = salario
        self.__formacao = formacao
        
    def setSalario(self, salario):
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
    def setFormacao(self, formacao):
        self.__formacao = formacao
        
    def getFormacao(self):
        return self.__formacao
    
    def info(self):
        super().info()  # executa o código da classe pai
        print("Formação =", self.__formacao)
        print("Salário =", self.__salario)

##########################################

#prof3 = Professor("Carla",31,3000,"Biologia")
#prof3.info()

#print(f'Hoje tem aula de {prof3.getFormacao()} com {prof3.getNome()}.')

'''    
prof1 = Professor()
prof1.setNome("Murilo")
prof1.setIdade(25)
prof1.setSalario(2000)
prof1.setFormacao("História")

print(f"Prof. {prof1.getNome()} ensina {prof1.getFormacao()}")
'''
