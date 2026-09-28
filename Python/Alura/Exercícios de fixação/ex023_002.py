numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

texto = f"""
Números: {numeros}
Maior: {maior}
Índice do maior: {numeros.index(maior)}
Menor: {menor}
Índice do menor: {numeros.index(menor)}
"""

print(texto)