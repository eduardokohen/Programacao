matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento da posição [{i} {j}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("\nMatriz:\n")

for linha in matriz:
    for elemento in linha:
        print(elemento, end = " ")
    print()