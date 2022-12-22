class Produto:
    
    def __init__(self, nome_t):
        self.nome = nome_t
        self.__estoque = 0
    
    def info(self):
        print(f"{self.nome} / {self.__estoque}")
    
    def incluir(self, qtd):
        self.__estoque += qtd
    
    def vender(self, qtd):
        self.__estoque -= qtd
        
###########################################
        
p1 = Produto("Nescau")
p1.incluir(5)
p1.info()
p1.incluir(2)
p1.info()
p1.vender(6)
p1.info()