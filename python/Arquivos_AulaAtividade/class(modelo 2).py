class Aluno:
    def __init__(self,  matricula: int , nome: str , sexo: str , idade: int ):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def dados(self):
        print(f'\nMatricula é: 000{self.matricula}. \nO nome é: {self.nome}. \nO sexo é {self.sexo}. \nA idade é : {self.idade} ')

perguntas = {
    "matricula": "Digite a matrícula do aluno: ",
    "nome": "Digite o nome do aluno: ",
    "sexo": "Digite o sexo do aluno (M/F): ",
    "idade": "Digite a idade do aluno: "
}

dados_aluno = {}
for chave, pergunta in perguntas.items():
    if chave == 'matricula' or chave == 'idade':
        valor = int(input(pergunta))
    else:
        valor=input(pergunta)
    dados_aluno[chave] = valor

aluno = Aluno(**dados_aluno)
aluno.dados()
