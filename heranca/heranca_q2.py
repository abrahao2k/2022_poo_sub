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
        if salario >= 0 :
            self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
    def info(self):
        print("Nome:", self.__nome)
        print("Salário:", self.__salario)


class Gerente(Empregado):
    __departamento = None
    
    def __init__(self, nome, salario, depto):
        super().__init__(nome,salario)
        self.__departamento = depto

    def setDepartamento(self, depto):
        self.__departamento = depto
    
    def getDepartamento(self):
        return self.__departamento
    
    def info(self):
        super().info()
        print("Departamento =", self.__departamento)


class Vendedor(Empregado):
    __comissao = 0
    
    def __init__(self,nome,salario,comissao):
        super().__init__(nome,salario)
        self.__comissao = comissao
    
    def setComissao(self, comissao):
        if comissao > 0 :
            self.__comissao = comissao
    
    def getComissao(self):
        return self.__comissao
    
    def calcularSalario(self):
        adicional = self.getSalario() * (self.__comissao/100)
        return self.getSalario() + adicional
    
    def info(self):
        super().info()
        print("Comissão =", self.__comissao, "%")
        print("Sal.+Comissão = R$", self.calcularSalario())
        
## TESTE VENDEDOR ##
vend1 = Vendedor("Caio",1950.00, 8)
vend1.info()

## TESTE GERENTE ##
#ger1 = Gerente("Bianca",3800.00,"Vendas")
#ger1.info()

## TESTE EMPREGADO ##
#emp1 = Empregado("Aluisio Brito", 2750.00)
#emp1.info()
    