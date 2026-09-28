numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

texto = f"""
Números: {numeros}
Pares: {pares}
Ímpares: {impares}
"""

print(texto)