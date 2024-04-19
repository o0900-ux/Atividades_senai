from pula_linha import *

pula_linha()

class Pessoa:
    def __init__(self,nome,sexo,cpf):
        self.nome=nome
        self.sexo=sexo
        self.cpf=cpf

    def comer(self):
        return f'{self.nome} esta comendo'
    
    def beber(self):
        return f'{self.nome} esta bebendo'
    
    def falar(self, mensagem):
        return f'{self.nome} esta falando: {mensagem}'
    
    def correr(self):
        return f'{self.nome} esta correndo'

if __name__ == '__main__':
    pessoa1 = Pessoa('eumesmo','|M','|123.456.789-00')
    pessoa2 = Pessoa('eumesmo(!)','|F','|123.456.789-00')
    print(pessoa1.nome, pessoa1.sexo, pessoa1.cpf)
    print(pessoa2.nome, pessoa2.sexo, pessoa2.cpf)

    pula_linha()

    print(pessoa1.comer())
    print(pessoa2.beber())
    print(pessoa1.falar('ola, como vai?'))
    print(pessoa2.correr())
    
pula_linha()

class Carro:
    def __init__(self,placa,modelo,ano):
        self.placa=placa
        self.modelo=modelo
        self.ano=ano
      
if __name__ == '__main__':
    palio= Carro('kjb-2668','edx','1997')
    vectra = Carro('kir-0932','elite','2008')
    dustern=Carro('oyw-4l08', 'Dynamic', '2015')
    print(palio.placa,vectra.placa, dustern.placa)
    print(palio.modelo,vectra.modelo, dustern.modelo)
    print(palio.ano,vectra.ano, dustern.ano)

pula_linha()
