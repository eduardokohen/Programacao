numeros = range(1,21)

for numero in numeros:
    if numero % 3 == 0:
        continue
    print(numero, end = " ")