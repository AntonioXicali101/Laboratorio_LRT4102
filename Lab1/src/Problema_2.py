# Solicita al usuario el número de horas trabajadas
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))

# Solicita la tarifa por hora
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

# Calcula el pago total
pago_total = horas_trabajadas * tarifa_por_hora

# Muestra el resultado
print(f"El pago correspondiente es: {pago_total}")
