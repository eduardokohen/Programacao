matriz = []

linha = int(input("Digite a quantidade de linhas da matriz: "))
coluna = int(input("Digite a quantidade de colunas da matriz: "))

for i in range(linha):
    linhas = []
    for j in range(coluna):
        num = int(input("Elemento {i+1} {j+1}: "))
        linhas.append(num)
    matriz.append(linhas)

for i in range(len(matriz)):
    soma = sum(matriz[i])
    print(f"Soma da linha {i+1}: {soma}.")