from classePessoa import Pessoa

class Aluno(Pessoa):
    __curso = None
    
    def setCurso(self,curso):
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
#######################

aluno1 = Aluno()
aluno1.setNome("Joaquim")
aluno1.setIdade(18)
aluno1.setCurso("Química")

print(f'{aluno1.getNome()} faz {aluno1.getCurso()}')