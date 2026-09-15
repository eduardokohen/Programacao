numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero > 10:
        print(f"O primeiro número maior que 10 é {numero}")
        break