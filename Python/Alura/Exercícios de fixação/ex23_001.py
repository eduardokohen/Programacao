numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número da lista: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero

texto = f"""
Números: {numeros}
Maior número: {maior}
Índice do maior número: {numeros.index(maior)}
Menor número: {menor}
Índice do menor número: {numeros.index(menor)}
"""

print(texto)