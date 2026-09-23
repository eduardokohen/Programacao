pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

texto = f"""
Números pares: {pares}.
Números ímpares: {impares}
"""

print(texto)