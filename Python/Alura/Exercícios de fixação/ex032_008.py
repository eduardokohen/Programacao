matriz = []

for i in range(3):
    linhas = []
    for j in range(3):
        num = int(input(f"Elemento {i+1} {j+1}: "))
        linhas.append(num)
    matriz.append(linhas)

print("\nMatriz:\n")

for linhas in matriz:
    for num in linhas:
        print(f"[{num}]", end=" ")
    print()

maior = matriz[0][0]
menor = matriz[0][0]

for linhas in matriz:
    for num in linhas:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"""O maior número da matriz é: {maior}.
      O menor número da matriz é: {menor}.""")