from datetime import datetime
import math
import tkinter as tk
from tkinter import simpledialog, scrolledtext

TOTAL_LUGARES = 83
lugares = {i: None for i in range(1, TOTAL_LUGARES + 1)}
receita_total = 0.0

def mostrar_lugares():
    output.delete(1.0, tk.END)
    for i, info in lugares.items():
        if info:
            if info['pago']:
                preco = info['preco']
                estado = "Pago"
            else:
                tempo = datetime.now() - info['entrada']
                horas = math.ceil(tempo.total_seconds() / 3600)
                preco = horas * 1.35
                estado = "Por pagar"
            output.insert(tk.END, f"Lugar {i}: {info['matricula']} | Entrada: {info['entrada'].strftime('%d/%m %H:%M')} | {estado} | {preco:.2f} €\n")
        else:
            output.insert(tk.END, f"Lugar {i}: [LIVRE]\n")

def registar_carro():
    mat = simpledialog.askstring("Matrícula", "Introduza a matrícula:", parent=w.tk)
    if not mat:
        return
    mat = mat.upper()
    for i, info in lugares.items():
        if info is None:
            agora = datetime.now()
            lugares[i] = {'matricula': mat, 'entrada': agora, 'pago': False, 'preco': 0.0}
            output.insert(tk.END, f"Carro {mat} registado no lugar {i} às {agora.strftime('%H:%M')}\n")
            return
    output.insert(tk.END, "Parque cheio!\n")

def marcar_pago():
    global receita_total
    mat = simpledialog.askstring("Pagamento", "Matrícula do carro a pagar:", parent=w.tk)
    if not mat:
        return
    mat = mat.upper()
    for info in lugares.values():
        if info and info['matricula'] == mat and not info['pago']:
            tempo = datetime.now() - info['entrada']
            horas = math.ceil(tempo.total_seconds() / 3600)
            preco = horas * 1.35
            info['pago'] = True
            info['preco'] = preco
            receita_total += preco
            output.insert(tk.END, f"{mat}: {horas}h x 1.35€ = {preco:.2f} €\n")
            return
    output.insert(tk.END, "Não encontrada ou já paga.\n")

def listar_nao_pagos():
    achou = False
    output.delete(1.0, tk.END)
    for i, info in lugares.items():
        if info and not info['pago']:
            output.insert(tk.END, f"Lugar {i}: {info['matricula']} (Entrada: {info['entrada'].strftime('%H:%M')})\n")
            achou = True
    if not achou:
        output.insert(tk.END, "Todos pagos.\n")

def remover_carro():
    mat = simpledialog.askstring("Remover carro", "Matrícula:", parent=w.tk)
    if not mat:
        return
    mat = mat.upper()
    for i, info in lugares.items():
        if info and info['matricula'] == mat:
            if not info['pago']:
                output.insert(tk.END, "⚠️ Ainda não pagou.\n")
            lugares[i] = None
            output.insert(tk.END, f"{mat} removido do lugar {i}.\n")
            return
    output.insert(tk.END, "Matrículaa não encontrada.\n")

def mostrar_receita():
    output.insert(tk.END, f"Receita total: {receita_total:.2f} €\n")


class MaximizaJanela:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.state('zoomed')
        self.frame = tk.Frame(self.tk)
        self.frame.pack()

        frame_botoes = tk.Frame(self.frame)
        frame_botoes.pack(pady=10)

        botoes = [
            ("Ver lugares", mostrar_lugares),
            ("Registar carro", registar_carro),
            ("Marcar pago", marcar_pago),
            ("Ver não pagos", listar_nao_pagos),
            ("Remover carro", remover_carro),
            ("Ver receita", mostrar_receita),
            ("Sair", self.tk.destroy)
        ]

        for texto, comando in botoes:
            tk.Button(frame_botoes, text=texto, command=comando, height=2, width=20, font=("Arial", 12)).pack(pady=5)

        global output
        output = scrolledtext.ScrolledText(self.frame, width=100, height=40, font=("Courier", 10))
        output.pack(pady=10)

if __name__ == '__main__':
    w = MaximizaJanela()
    w.tk.mainloop()