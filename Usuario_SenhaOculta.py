import getpass

class Usuario:
    def __init__(self, nome_t, senha_t):
        self.nome = nome_t       # public
        self.__senha = senha_t   # private

    def validar(self, senha_t):
        if senha_t == self.__senha:
            print("Acesso permitido.")
        else:
            print("Acesso negado.")
#########################################
nome = input("Nome: ")
senha = getpass.getpass(prompt="Senha: ")
user1 = Usuario(nome,senha)
user1.validar("456")
