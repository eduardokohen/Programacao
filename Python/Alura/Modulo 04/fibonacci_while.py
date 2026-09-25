limite_valor = int(input("Informe o limite: "))

fibonacci = [0,1]
indice = 2

while True:
    proximo = fibonacci[indice - 1] + fibonacci[indice - 2]

    if proximo > limite_valor:
        break
    fibonacci.append(proximo)
    indice = indice + 1

print(fibonacci)