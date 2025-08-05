from datetime import datetime, timedelta
import math

TOTAL_LUGARES = 83
lugares = {i: None for i in range(1, TOTAL_LUGARES + 1)}
receita_total = 0.0

def mostrar_lugares():
    for i, info in lugares.items():
        if info:
            estado = "Pago" if info['pago'] else "Por pagar"
            print(f"Lugar {i}: {info['matricula']} | Entrada: {info['entrada'].strftime('%d/%m %H:%M')} | {estado} | {info['preco']:.2f} €")
        else:
            print(f"Lugar {i}: [LIVRE]")

def registar_carro():
    mat = input("Matrícula: ").upper()
    for i, info in lugares.items():
        if info is None:
            agora = datetime.now()
            lugares[i] = {'matricula': mat, 'entrada': agora, 'pago': False, 'preco': 0.0}
            print(f"Carro {mat} no lugar {i} às {agora.strftime('%H:%M')}")
            return
    print("Parque cheio!")

def marcar_pago():
    global receita
    mat = input("Matrícula: ").upper()
    for info in lugares.values():
        if info and info['matricula'] == mat and not info['pago']:
            tempo = datetime.now() - info['entrada']
            horas = math.ceil(tempo.total_seconds() / 3600)
            preco = horas * 1.35
            info['pago'] = True
            info['preco'] = preco
            receita += preco
            print(f"{mat}: {horas}h x 1.35€ = {preco:.2f} €")
            return
    print("Não encontrada ou já paga.")

def listar_nao_pagos(): #função para marcar os que nao pagaram, tenho que fazer com que peça a matricula e mostre as horas e quando nao estao pagos

def remover_carro(): #função para removar os careros que ja pagaram e trocar automaticamente para None

def mostrar_receita(): #função para mostrar quanto o parque deu no total (acrescentar o diario e mensal, ou semanal até)

def menu(): 