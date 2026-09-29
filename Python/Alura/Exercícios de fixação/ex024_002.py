numeros = []
unicos = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero not in unicos:
        unicos.append(numero)

print(numeros)
print(unicos)