from random import *
from tkinter import *

def mega_sena():

    tela.delete(1.0, END)
    
    tela.insert(END, 'Seus numeros(1): \n', 'center')
    for _ in range(6):
        valores = randint(1,60)
        tela.insert(END, str( valores) + ',', 'center')

    tela.insert(END, '\n\n')

    tela.insert(END, 'Seus numeros(2): \n', 'center')
    for _ in range(6):
        valores = randint(1,60)
        tela.insert(END, str( valores) + ',', 'center')

    tela.insert(END, '\n\n')

    tela.insert(END, 'Seus numeros(3): \n', 'center')
    for _ in range(6):
        valores = randint(1,60)
        tela.insert(END, str( valores) + ',', 'center')


root = Tk()
root.title("Mega Sema")

tela = Text(root, height=8, width=20)
tela.pack()

tela.tag_configure('center', justify='center')
tela.insert(END, 'MEGA SENA', 'center')
tela.insert(END, """
    __
 __/o \_
(______/ \\
   _ |_   \\
  /     \\__/
""", 'center')

valores = Button(root, text="Numeros para a Mega Sena", command=mega_sena)
valores.pack()

root.mainloop()
