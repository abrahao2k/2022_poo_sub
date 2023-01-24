from tkinter import *

janela = Tk()
janela.geometry("500x250+100+100")
janela.title("Programa da NASA 1.0")
#janela.resizable(FALSE, FALSE)
janela.minsize(300,150)
janela.maxsize(600,350)

texto1 = "Esse é\num texto\ncom várias\nlinhas."
rot1 = Label(janela, text = texto1, justify="left")
rot1.grid(row=0, column=0)
texto2 = """Esse texto
também tem
várias linhas."""
rot2 = Label(janela, text = texto2, justify="right")
rot2.grid(row=1, column=1)

imagem = PhotoImage(file="ifrn.png")
rot3 = Label(janela, image = imagem)
rot3.grid(row=2,column=2)


janela.mainloop()