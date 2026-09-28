numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

texto = f"""
Todos os números da lista: {numeros}
Maior número da lista: {maior}
Índice do maior número: {numeros.index(maior)}
Menor número da lista: {menor}
Índice do menor número: {numeros.index(menor)}
"""

print(texto)