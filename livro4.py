class Livro:
    def __init__(self, pTitulo, pAutor, pAno):
        self.titulo = pTitulo
        self.autor = pAutor
        self.ano = pAno
        self.pagina = 1
    
    def info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Página atual: {self.pagina}\n")
        
    def passarPagina(self):
        self.pagina += 1
        
    def voltarPagina(self):
        if self.pagina > 1:
            self.pagina -= 1
        
##############################################
livro4 = Livro("O Hobbit", "J.R.R.Tolkien", 1949)
livro4.info()
for x in range(8):
    livro4.passarPagina()
    livro4.info()
livro4.voltarPagina()
livro4.info()