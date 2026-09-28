numeros = []

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número da lista: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

texto = f"""
Lista de todos os números: {numeros}
Maior número da lista: {maior}
Índice do maior número: {numeros.index(maior)}
Menor número da lista: {menor}
Índice do menor número da lista: {numeros.index(menor)}
"""

print(texto)