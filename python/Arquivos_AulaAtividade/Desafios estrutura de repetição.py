print('--------desafio1-------')
p=input('digite: ')

v='aeiouAEIOU'
n_v=0
n_c=0

for l in p:
    if l.isalpha():
        if l in v:
            n_v += 1
        else:
            n_c +=1

print("Número de vogais: ",n_v, "\nNúmero de consoantes: ", n_c, '\n--------fim-------')

print('--------desafio2-------')
dias_uteis = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
dias_digitados = []

for i in range(7):
    dia = input("Digite o dia da semana: ").capitalize()
    if dia in dias_uteis:
        dias_digitados.append(dia + "-feira")

print("\nDias uteis:")
for dia in dias_digitados:
    print(dia)
print('--------fim-------')

print('--------desafio3-------')
numero = int(input("Digite um numero  para verificar se e primo: "))

if numero <= 1:
    print(numero, "não e um numero primo.")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero, "e um numero primo.")
    else:
        print(numero, "não e um numero primo.")
print('--------fim-------')





