class Aluno:
    def __init__(self,  matricula: int , nome: str , sexo: str , idade: int ):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def dados(self):
        print(f'\nMatricula é: 000{self.matricula}. \nO nome é: {self.nome}. \nO sexo é {self.sexo}. \nA idade é : {self.idade} ')
    
aluno = Aluno(matricula=23522 ,nome='Gabriel' , sexo='M'  , idade=17 )
aluno.dados()
