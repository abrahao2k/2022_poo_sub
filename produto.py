class Produto:
    def __init__(self, pNome, pPreco, pEstoque):
        self.nome = pNome
        self.preco = pPreco
        self.estoque = pEstoque
    
    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self.estoque}\n")
    
    def vender(self):
        if self.estoque > 0 :
            self.estoque -= 1
        else:
            print("Sem estoque deste produto.")

p1 = Produto("Caneta", 2.90, 15)
p1.info()
p1.vender()
p1.info()