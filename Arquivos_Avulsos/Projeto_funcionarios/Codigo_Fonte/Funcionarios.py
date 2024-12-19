import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random

def cadastrar_funcionario():
    nome = entry_nome.get()
    setor = combo_setor.get()
    id_funcionario = entry_id.get()

    if not nome or not setor or not id_funcionario:
        messagebox.showerror("Erro", "Nome, setor e ID do funcionário são campos obrigatórios.")
        return

    if len(id_funcionario) != 8:
        messagebox.showerror("Erro", "O ID deve conter exatamente 8 dígitos.")
        return

    for func in funcionarios:
        if func['id'] == id_funcionario and func['setor'] == setor:
            messagebox.showerror("Erro", "Já existe um funcionário com o mesmo ID e setor.")
            return

    funcionario = {
        'nome': nome,
        'setor': setor,
        'id': id_funcionario,
        'salario': None,
        'dias_trabalho': None,
        'tempo_trabalho': None,
        'horario_entrada_saida': None,
    }

    funcionarios.append(funcionario)
    salvar_funcionarios()
    atualizar_tabela()

    entry_nome.delete(0, tk.END)
    combo_setor.set('')
    entry_id.delete(0, tk.END)

def gerar_id_aleatorio():
    id_aleatorio = str(random.randint(10000000, 99999999))
    entry_id.delete(0, tk.END)
    entry_id.insert(0, id_aleatorio)

def pesquisar_funcionario():
    nome_pesquisa = entry_pesquisar_nome.get().lower()
    funcionarios_encontrados = [func for func in funcionarios if nome_pesquisa in func['nome'].lower()]
    mostrar_funcionarios_encontrados(funcionarios_encontrados)
    print("Funcionários Encontrados:", funcionarios_encontrados)

def mostrar_funcionarios_encontrados(funcionarios_encontrados):
    tree.delete(*tree.get_children())
    for func in funcionarios_encontrados:
        tree.insert('', tk.END, values=(func['nome'], func['setor'], func['id']))
    print("Tabela Atualizada com Funcionários Encontrados:", funcionarios_encontrados)

def salvar_funcionarios():
    with open('funcionarios.json', 'w') as file:
        json.dump(funcionarios, file)

def carregar_funcionarios():
    try:
        with open('funcionarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def deletar_funcionario():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um funcionário para excluir.")
        return

    index = int(tree.index(selected_item))
    del funcionarios[index]
    salvar_funcionarios()
    atualizar_tabela()

def adicionar_informacoes_adicionais():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um funcionário para adicionar informações adicionais.")
        return

    index = int(tree.index(selected_item))
    funcionario = funcionarios[index]

    salario = simpledialog.askfloat("Adicionar Informações", "Digite o salário mensal:")
    dias_trabalho = simpledialog.askstring("Adicionar Informações", "Digite os dias de trabalho:")
    tempo_trabalho = simpledialog.askstring("Adicionar Informações", "Digite o tempo de trabalho:")
    horario_entrada_saida = simpledialog.askstring("Adicionar Informações", "Digite o horário de entrada/saída:")

    funcionario['salario'] = salario
    funcionario['dias_trabalho'] = dias_trabalho
    funcionario['tempo_trabalho'] = tempo_trabalho
    funcionario['horario_entrada_saida'] = horario_entrada_saida

    salvar_funcionarios()
    atualizar_tabela()

def on_double_click(event):
    item = tree.selection()[0]
    id_funcionario = tree.item(item, "values")[2]
    funcionario = next((func for func in funcionarios if func['id'] == id_funcionario), None)

    if funcionario:
        informacoes = f"Informações do Funcionário:\n\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nID: {funcionario['id']}\n\n"
        if funcionario['salario'] is not None:
            informacoes += f"Salário Mensal: {funcionario['salario']}\n"
        if funcionario['dias_trabalho'] is not None:
            informacoes += f"Dias de Trabalho: {funcionario['dias_trabalho']}\n"
        if funcionario['tempo_trabalho'] is not None:
            informacoes += f"Tempo de Trabalho: {funcionario['tempo_trabalho']}\n"
        if funcionario['horario_entrada_saida'] is not None:
            informacoes += f"Horário de Entrada/Saída: {funcionario['horario_entrada_saida']}"

        messagebox.showinfo("Informações do Funcionário", informacoes)
    else:
        messagebox.showwarning("Aviso", "Funcionário não encontrado.")
    print("Informações do Funcionário Exibidas:", funcionario)

def atualizar_tabela():
    tree.delete(*tree.get_children())
    for func in funcionarios:
        tree.insert('', tk.END, values=(func['nome'], func['setor'], func['id']))


root = tk.Tk()
root.title("Cadastro de Funcionários")

funcionarios = carregar_funcionarios()

label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_setor = tk.Label(root, text="Setor:")
combo_setor = ttk.Combobox(root, values=["Amarelo", "Azul", "Laranja"])

label_id = tk.Label(root, text="ID:")
entry_id = tk.Entry(root)
button_gerar_id = tk.Button(root, text="Gerar ID Aleatório", command=gerar_id_aleatorio)

button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_funcionario)

label_nome.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_setor.grid(row=1, column=0, sticky="e", padx=5, pady=5)
combo_setor.grid(row=1, column=1, padx=5, pady=5)

label_id.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_id.grid(row=2, column=1, padx=5, pady=5)
button_gerar_id.grid(row=2, column=2, padx=5, pady=5)

button_cadastrar.grid(row=3, column=0, columnspan=3, pady=10)

tree = ttk.Treeview(root, columns=("Nome", "Setor", "ID"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Setor", text="Setor")
tree.heading("ID", text="ID")
tree.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

label_pesquisar_nome = tk.Label(root, text="Pesquisar por nome:")
entry_pesquisar_nome = tk.Entry(root)
button_pesquisar_nome = tk.Button(root, text="Pesquisar", command=pesquisar_funcionario)

label_pesquisar_nome.grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_pesquisar_nome.grid(row=5, column=1, padx=5, pady=5)
button_pesquisar_nome.grid(row=5, column=2, padx=5, pady=5)

button_excluir = tk.Button(root, text="Excluir Funcionário", command=deletar_funcionario)
button_excluir.grid(row=6, column=0, columnspan=3, pady=10)

button_adicionar_informacoes = tk.Button(root, text="Adicionar Informações Adicionais", command=adicionar_informacoes_adicionais)
button_adicionar_informacoes.grid(row=7, column=0, columnspan=3, pady=10)

tree.bind("<Double-1>", on_double_click)

atualizar_tabela()

root.mainloop()
