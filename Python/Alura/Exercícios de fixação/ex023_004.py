numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

texto = f"""
Números da lista: {numeros}
Maior número da lista: {maior}
Índice do maior número: {numeros.index(maior)}
Menor número da lista: {menor}
Índice do menor número da lista: {numeros.index(menor)}
"""

print(texto)