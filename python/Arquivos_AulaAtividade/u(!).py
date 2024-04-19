from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo

root = Tk()
root.title("CALCULADORA")
root.geometry("300x300")
tela =Text(root)
tela.pack(padx=30, pady=30, fill='x', expand=True)

n1 =tk.StringVar()
n2 =tk.StringVar()

def soma():

    valor1=float(n1.get())  
    valor2=float(n2.get())  

    resutado=valor1+valor2

    fim=f'Seu resutado: {resutado} '
    showinfo(
        title='Information',
        message=fim
    )

def subtracao():

    valor1=float(n1.get())  
    valor2=float(n2.get())  

    resutado=valor1-valor2

    fim=f'Seu resutado: {resutado} '
    showinfo(
        title='Information',
        message=fim
    )

def multiplicacao():

    valor1=float(n1.get())  
    valor2=float(n2.get())  

    resutado=valor1*valor2

    fim=f'Seu resutado: {resutado} '
    showinfo(
        title='Information',
        message=fim
    )

def divisao():

    valor1=float(n1.get())  
    valor2=float(n2.get())  

    resutado=valor1/valor2

    fim=f'Seu resutado: {resutado} '
    showinfo(
        title='Information',
        message=fim
    )

numero1=Label(tela, text="1° Digito")
numero1.pack(expand=True)

n1=Entry(tela, textvariable=n1)
n1.pack(expand=True)


numero2=Label(tela, text="\n2° Digito")
numero2.pack(expand=True)

n2=Entry(tela, textvariable=n2)
n2.pack(expand=True)

soma = Button(tela, text="Soma", command=soma)
soma.pack(expand=True)

subtracao = Button(tela, text="Subtração", command=subtracao)
subtracao.pack(expand=True)

multiplicacao = Button(tela, text="Multiplicação", command=multiplicacao)
multiplicacao.pack(expand=True)

divisao = Button(tela, text="Divisão", command=divisao)
divisao.pack(expand=True)


root.mainloop()