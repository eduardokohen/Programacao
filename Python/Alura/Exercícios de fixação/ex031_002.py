matriz = []

linha = int(input("Digite a quantidade de linhas da matriz: "))
coluna = int(input("Digite a quantidade de colunas da matriz: "))

for i in range(linha):
    linhas = []
    for j in range(coluna):
        num = int(input(f"Elemento {i+1} {j+1}: "))
        linhas.append(num)
    matriz.append(linhas)

for linhas in matriz:
    soma = sum(linhas)
    print(f"Soma da linha: {soma}.")