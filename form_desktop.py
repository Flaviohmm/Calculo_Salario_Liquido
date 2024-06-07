import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

entry_salario_base = None
entry_vale_refeicao = None
entry_vale_transporte = None

label_resultado = None

# Função para calcular o salário líquido
def calcular_salario_liquido():
    salario_base = float(entry_salario_base.get())
    vale_refeicao = float(entry_vale_refeicao.get())
    vale_transporte = float(entry_vale_transporte.get())

    salario_bruto = salario_base + vale_refeicao + vale_transporte
    inss = salario_bruto * 0.11

    # Cálculo do IRPF conforme faixa de imposto de renda
    # Aqui você pode adicionar a lógica para calcular o IRPF

    salario_liquido = salario_bruto - inss # Exemplo simples, sem considerar o IRPF

    label_resultado.config(text=f'Salário Líquido: R$ {salario_liquido:.2f}')

# Configuração da interface gráfica
root = tk.Tk()
style = Style("cosmo") # Escolha o tema desejado

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

ttk.Label(frame, text="Salário Base:").grid(row=0, column=0)
entry_salario_base = ttk.Entry(frame)
entry_salario_base.grid(row=0, column=1)

ttk.Label(frame, text="Vale Refeição:").grid(row=1, column=0)
entry_vale_refeicao = ttk.Entry(frame)
entry_vale_refeicao.grid(row=1, column=1)

ttk.Label(frame, text="Vale Transporte:").grid(row=2, column=0)
entry_vale_transporte = ttk.Entry(frame)
entry_vale_transporte.grid(row=2, column=1)

ttk.Button(frame, text="Calcular Salário Líquido", command=calcular_salario_liquido).grid(row=3, column=0, columnspan=2, pady=10)

label_resultado = ttk.Label(frame, text='')
label_resultado.grid(row=4, column=0, columnspan=2)

root.mainloop()