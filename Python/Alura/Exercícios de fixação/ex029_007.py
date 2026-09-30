matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o elemento da posição [{i+1} {j+1}]: "))
        linha.append(num)
    matriz.append(linha)

print("\nMatriz:\n")

for linha in matriz:
    for num in linha:
        print(num, end=" ")
    print()

for linha in matriz:
    for num in linha:
        soma += num

print(f"A soma de todos elementos da matriz é {soma}.")