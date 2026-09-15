numeros = []

for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

soma = 0
maior = numeros[0]
menor = numeros[0]
pares = 0
impares = 0

for numero in numeros:

    soma = soma + numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")