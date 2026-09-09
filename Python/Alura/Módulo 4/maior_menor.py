numeros = []

for i in range(7):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

if len(numeros) > 0:
    maior = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    dif = maior - menor

print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")
print(f"A diferença entre o maior e o menor é de {dif}.")