matriz = []

linha = int(input("Digite a quantidade de linhas: "))
coluna = int(input("Digite a quantidade de colunhas: "))

for i in range(linha):
    linhas = []
    for j in range(coluna):
        num = int(input(f"Elemento [{i+1} {j+1}]: "))
        linhas.append(num)
    matriz.append(linhas)

soma = sum(sum(linhas) for linhas in matriz)

print("\nMatriz:\n")

for linhas in matriz:
    for num in linhas:
        print(num, end=" ")
    print()

print(f"A soma de todos os elementos da matriz é: {soma}.")