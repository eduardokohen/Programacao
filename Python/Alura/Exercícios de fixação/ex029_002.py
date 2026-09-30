matriz = []

for i in range(3):
    linhas = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento da posição [{i} {j}]: "))
        linhas.append(elemento)
    matriz.append(linhas)

soma = sum(matriz[0]) + sum(matriz[1]) + sum(matriz[2])

print(f"A soma de todos elementos da matriz é: {soma}.")