numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número da lista: "))
    numeros.append(numero)

menor = numeros[0]
maior = numeros[0]

for numero in numeros:
    if menor > numero:
        menor = numero
    if maior < numero:
        maior = numero

texto = f"""
Lista dos números: {numeros}
Maior número da lista: {maior}
Índice do maior número da lista: {numeros.index(maior)}
Menor número da lista: {menor}
Índice do menor número da lista: {numeros.index(menor)}
"""

print(texto)