import time
import pygame


pygame.init()


pygame.mixer.music.load('Tarzan.mp3')


pygame.mixer.music.play(-1)

texto = """
Tarzan.
\n
Quem foi que disse que eu era forte?
Nunca pratiquei esporte, nem conheço futebol...
O meu parceiro sempre foi o travesseiro
E eu passo o ano inteiro sem ver um raio de sol
A minha força bruta reside
Em um clássico cabide, já cansado de sofrer
Minha armadura é de casimira dura
Que me dá musculatura, mas que pesa e faz doer
\n
Eu poso pros fotógrafos, e destribuo autógrafos
A todas as pequenas lá da praia de manhã
Um argentino disse, me vendo em Copacabana:
'No hay fuerza sobre-humana que detenga este Tarzan'
\n
De lutas não entendo abacate
Pois o meu grande alfaiate não faz roupa pra brigar
Sou incapaz de machucar uma formiga
Não há homem que consiga nos meus músculos pegar
Cheguei até a ser contratado
Pra subir em um tablado, pra vencer um campeão
Mas a empresa, pra evitar assassinato
Rasgou logo o meu contrato quando me viu sem roupão
\n
Eu poso pros fotógrafos, e destribuo autógrafos
A todas as pequenas lá da praia de manhã
Um argentino disse, me vendo em Copacabana:
'No hay fuerza sobre-humana que detenga este Tarzan'
\n
Quem foi que disse que eu era forte?
Nunca pratiquei esporte, nem conheço futebol...
O meu parceiro sempre foi o travesseiro
E eu passo o ano inteiro sem ver um raio de sol
A minha força bruta reside
Em um clássico cabide, já cansado de sofrer
Minha armadura é de casimira dura
Que me dá musculatura, mas que pesa e faz doer
"""

frases = texto.split("\n\n")

for frase in frases:
    print(frase)
    time.sleep(15)


pygame.mixer.music.stop()

