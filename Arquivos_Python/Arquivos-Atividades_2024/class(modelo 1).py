class Aluno:
    def __init__(self,  matricula: int , nome: str , sexo: str , idade: int ):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

if __name__ == '__main__':
    aluno = Aluno(matricula=23522 ,nome='Gabriel' , sexo='M'  , idade=17 )
    print(f'\nMatricula é: {aluno.matricula}. \nO nome é: {aluno.nome}. \nO sexo é {aluno.sexo}. \nA idade é : {aluno.idade} ')
    
