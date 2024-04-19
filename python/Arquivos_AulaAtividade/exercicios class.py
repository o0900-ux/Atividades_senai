# Gabriel alexandre e emiily leticia.
# Atividades de classes.
def pular_linha():
     print('\n')
#questão 1.
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor 

    def ligar(self):
            return f'ligar o carro: {self.modelo} e de marca {self.marca}'
        
    def desligar(self):
            return f'desligar o carro: {self.modelo} e de ano {self.ano}'
        
    def acelerar(self):
            return f"acelerar o carro: {self.modelo} e de cor {self.cor}"
        
if __name__ == '__main__':
    carros = Carro('fiat','Palio','1997','plata')

    print(carros.ligar())
    print(carros.desligar())
    print(carros.acelerar())

#questão 2.
class Animal:
    def __init__(self, nome, idade, especie):
        self.nome=nome
        self.idade=idade
        self.especie=especie

    def emitir_som(self):
        return f'o animal de nome {self.nome} estar fazendo barulho'
        
    def mostra_informacoes(self):
        return f'o animal que fez barulho e da especie {self.especie}, tem a idade de {self.idade}, e tem o nome {self.nome}'
        
if __name__ == '__main__':
    animal = Animal('beethoven','11','cachorro')
    pular_linha()
    print(animal.emitir_som())
    print(animal.mostra_informacoes())

#questão 3.
class Conta_bancaria:
    def __init__(self, numero_da_conta, saldo, titular):
         self.numero_da_conta=numero_da_conta
         self.saldo=saldo
         self.titular=titular

    def depositar(self, valor):
         self.saldo += valor
         return f'depósito de R$ {valor} realizado com sucesso\nsaldo atual: R$ {self.saldo}'
    
    def sacar(self, valor):
        self.saldo -= valor
        return f'saque de R$ {valor} realizado com sucesso\nsaldo atual: R$ {self.saldo}' 
    
if __name__ == '__main__':
    conta = Conta_bancaria('0987656',11,'pessoa humana')
    pular_linha()
    print(conta.depositar(100))
    print(conta.sacar(50))

#questão 4.
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def compra(self, produtos):
         self.produtos=produtos
         self.preco *= produtos
         return f'o total da compra de {produtos} prudutos foi de R$ {self.preco}'

    def estoque_final(self):
        self.estoque -= self.produtos
        return f'quantidade de itens ainda em estoque de {self.estoque}'

if __name__ == '__main__':
    loja = Produto('remedio',11.55,50)
    pular_linha()
    print(loja.compra(2))
    print(loja.estoque_final())

#questão 5.
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        todos=self.lado1 + self.lado2 + self.lado3
        return f'o perimetro e igual: {todos}'

    def area(self):
        todos=self.lado1 + self.lado2 + self.lado3 / 2
        return f'o perimetro e igual: {todos}'

if __name__ == '__main__':
    lados = Triangulo(13,11,5)
    pular_linha()
    print(lados.perimetro())
    print(lados.area())
