class Ingresso:
    valor = 0.0
    def info(self):
        print("Valor = R$", self.valor)

class IngressoVIP(Ingresso):
    valorAdicional = 0.0
    def info(self):
        print("Valor VIP = R$",
        self.valor + self.valorAdicional)

## TESTE INGRESSO VIP ##
vip1 = IngressoVIP()
vip1.valor = 30.00
vip1.valorAdicional = 15.00
vip1.info()

## TESTE INGRESSO ##
#ingresso1 = Ingresso()
#ingresso1.valor = 30.0
#ingresso1.info()