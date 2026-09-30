matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o elemento da posição [{i+1} {j+1}]: "))
        linha.append(num)
    matriz.append(linha)

soma = sum(sum(linha) for linha in matriz)

print("\nMatriz:\n")

for linha in matriz:
    for num in linha:
        print(num, end = " ")
    print()

print(f"A soma de todos os termos da matriz é {soma}.")