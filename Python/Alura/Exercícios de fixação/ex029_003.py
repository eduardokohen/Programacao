matriz = []

for i in range(3):
    linhas = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento da posição [{i} {j}]: "))
        linhas.append(elemento)
    matriz.append(linhas)

soma = sum(sum(linha) for linha in matriz)

print("\nMatriz:\n")

for linhas in matriz:
    for elemento in linhas:
        print(elemento, end = " ")
    print()

print(f"A soma de todos elementos da matriz é: {soma}")