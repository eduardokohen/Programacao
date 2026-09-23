pares = []
impares = []

for i in range(10):
    num = int(input(f"Informe o {i+1}º número: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

texto = f"""
Números pares: {pares}
Números ímpares: {impares}
"""

print(texto)