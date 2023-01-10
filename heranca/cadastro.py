from classePessoa import Pessoa

p1 = Pessoa()
p1.setNome("Abelardo")
p1.setIdade(25)

print(f'Olá, {p1.getNome()}!')
print(f'Você tem {p1.getIdade()} anos.')