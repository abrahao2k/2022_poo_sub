class Veiculo:
    def __init__(self, pfabricante, pmodelo, pano):
        self.fabricante = pfabricante
        self.modelo = pmodelo
        self.ano = pano
    
###################################################
v1 = Veiculo("Fiat","Palio",2020)

print(f"Eu comprei um {v1.modelo}, ano {v1.ano}.")
