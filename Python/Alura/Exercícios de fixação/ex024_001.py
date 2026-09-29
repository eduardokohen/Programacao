numeros = []
unicos = []

for i in range(9):
    numero = int(input(f"Digite o {i+1}º número da lista: "))
    numeros.append(numero)

for numero in numeros:
    if numero not in unicos:
        unicos.append(numero)

print(unicos)