class Livro:
    def __init__(self, pTitulo, pAutor, pAno):
        self.titulo = pTitulo
        self.autor = pAutor
        self.ano = pAno
##############################################

livro3 = Livro("1984","George Orwell", 1948)

print(f"Você leu {livro3.titulo} de {livro3.autor}?")

