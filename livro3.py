class Livro:
    def __init__(self, pTitulo, pAutor, pAno):
        self.titulo = pTitulo
        self.autor = pAutor
        self.ano = pAno
    
    def info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
##############################################
livro4 = Livro("O Hobbit", "J.R.R.Tolkien", 1949)
livro4.info()