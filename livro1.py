class Livro:
    titulo = ""
    autor = ""
    ano = ""
#######################

livro1 = Livro()
livro1.titulo = "Presepadas de João Grilo"
livro1.autor = "Ariano Suassuna"
livro1.ano = 1985

livro2 = Livro()
livro2.titulo = "Python para Zumbis"
livro2.autor = "Jose Morreu"
livro2.ano = 2021

print(f"Eu tenho livros de {livro1.autor} e {livro2.autor}.")