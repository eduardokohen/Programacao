matriz = []
soma = 0

linha = int(input("Digite a quantidade de linhas da matriz: "))
coluna = int(input("Digite a quantidade de colunas da matriz: "))

for i in range(linha):
    linhas = []
    for j in range(coluna):
        num = int(input(f"Digite o elemento da posição [{i+1} {j+1}]: "))
        linhas.append(num)
    matriz.append(linhas)

print("\nMatriz:\n")

for linhas in matriz:
    for num in linhas:
        print(num, end=" ")
    print()

for linhas in matriz:
    for num in linhas:
        soma += num

print(f"A soma de todos elementos da matriz é: {soma}.")