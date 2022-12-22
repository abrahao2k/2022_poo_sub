class ContaBancaria:
    titular = ""
    saldo = 0
    senha = ""
    
    def depositar(self):
        valor = float(input("Valor do depósito? "))
        self.saldo += valor
        print("Depósito realizado.")
    
    def sacar(self):
        valor = float(input("Valor do saque? "))
        senha_t = input("Senha? ")
        if self.senha == senha_t:
            if self.saldo >= valor:
                self.saldo -= valor
                print("Saque efetuado.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Senha incorreta.")
    
    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo}")
# =============================================== #

c1 = ContaBancaria()
c1.titular = "Belarmino"
c1.senha = "0203"

c1.extrato()
c1.depositar()
c1.extrato()
c1.sacar()
c1.extrato()