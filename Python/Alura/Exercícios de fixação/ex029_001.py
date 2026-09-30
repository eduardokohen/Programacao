soma = 0
matriz = []

for i in range(3):
    linhas = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento da posição [{i} {j}]: "))
        linhas.append(elemento)
    matriz.append(linhas)

for linhas in matriz:
    for elemento in linhas:
        soma += elemento
print("A soma de todos elementos da matriz é:", soma)