class Empregado:
    __nome = None
    __salario = 0.0
    
    def __init__(self,nome,salario):
        self.__nome = nome
        self.__salario = salario
    
    def setNome(self,nome):
        self.__nome = nome
        
    def getNome(self):
        return self.__nome
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
    def info(self):
        print("Nome:", self.__nome)
        print("Salário:", self.__salario)

## TESTE EMPREGADO ##
emp1 = Empregado("Aluisio Brito", 2750.00)
emp1.info()
    