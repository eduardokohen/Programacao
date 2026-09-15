numeros = []

for i in range (8):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = 0
media = 0
pares = 0
impares = 0
maior = numeros[1]
menor = numeros[1]

for numero in numeros:
    soma = soma + numero
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

media = soma/len(numeros)

print("="*60)
print("Estatísticas".center(60))
print("="*60)

print(f"A lista de numeros é: {numeros}.")
print(f"A soma de todos os termos é: {soma}.")
print(f"A média dos termos é: {media:.2f}.")
print(f"O maior valor é: {maior}.")
print(f"O menor valor é: {menor}.")
print(f"Há {pares} números pares e {impares} números ímpares.")