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

def listar_nao_pagos():
    achou = False
    for i, info in lugares.items():
        if info and not info['pago']:
            print(f"Lugar {i}: {info['matricula']} (Entrada: {info['entrada'].strftime('%H:%M')})")
            achou = True
    if not achou:
        print("Todos pagos.")

def remover_carro():
    mat = input("Matrícula: ").upper()
    for i, info in lugares.items():
        if info and info['matricula'] == mat:
            if not info['pago']:
                print("⚠️ Ainda não pagou.")
            lugares[i] = None
            print(f"{mat} removido do lugar {i}.")
            return
    print("Matrícula não encontrada.")

def mostrar_receita():
       print(f"Receita total: {receita:.2f} €")
       
def menu():
    while True:
        print("\n=== MENU PARQUE ===")
        print("1. Ver lugares")
        print("2. Registar carro")
        print("3. Marcar pago")
        print("4. Ver não pagos")
        print("5. Remover carro")
        print("6. Ver receita")
        print("0. Sair")

        op = input("Escolha: ")

        if op == '1':
            mostrar_lugares()
        elif op == '2':
            registar_carro()
        elif op == '3':
            marcar_pago()
        elif op == '4':
            listar_nao_pagos()
        elif op == '5':
            remover_carro()
        elif op == '6':
            mostrar_receita()
        elif op == '0':
            break
        else:
            print("Opção inválida.")

menu()