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