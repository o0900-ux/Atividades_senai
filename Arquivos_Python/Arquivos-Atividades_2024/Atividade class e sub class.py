class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        return f'o veiculo de modelo "{self.modelo}" e de marca "{self.marca}" estar freando'
    
    def acelerar(self):
        return f'o veiculo de modelo "{self.modelo}" e de marca "{self.marca}" estar acelerando'
    
class Carro(Veiculo):
    def __init__(self, cor, marca, modelo):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        return f'o veiculo de modelo "{self.modelo}" de marca "{self.marca}" de cor "{self.cor}" abriu a porta'
    
class Moto(Veiculo):
    def __init__(self, cilindrada, marca, modelo):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def enpinar(self):
        return f'a moto de  modelo "{self.modelo}" de marca "{self.marca}" de cilindrada "{self.cilindrada}" estar enpinando'
    
if __name__ == '__main__':
    carros = Carro('cinza', 'fiat', 'uno')  
    print(carros.acelerar())
    print(carros.frear())
    print(carros.abrir_porta())

def pular_linha():
    return f'\n'

if __name__ == '__main__':
    print(pular_linha())
    motos = Moto('300', 'Honda', 'c100')
    print(motos.acelerar())
    print(motos.frear())
    print(motos.enpinar())   


    
