def main():
    """
    Calcula el pago total de cada operador en una lista.
    (nombre, sueldo_hora, horas_trabajadas).
    """
    
    # Lista de operadores
    personal = [
        ("Antonio", 10, 40),
        ("José", 8, 40),
        ("Ariadna", 8.5, 45),
        ("Bryan", 12, 30),
        ("Andrea", 13.5, 38),
        ("Alexa", 10.5, 44)
    ]

    # Recorremos la lista y calculamos la paga de cada operador
    for nombre_operador, tarifa_hora, horas_totales in personal:
        pago_total = tarifa_hora * horas_totales
        print(f"{nombre_operador} recibirá un pago de: {pago_total}")

if __name__ == "__main__":
    main()
