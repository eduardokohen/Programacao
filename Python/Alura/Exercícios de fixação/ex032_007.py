matriz = []

linha = int(input("Digite a quantidade de linhas da matriz: "))
coluna = int(input("Digite a quantidade de colunas da matriz: "))

for i in range(linha):
    linhas = []
    for j in range(coluna):
        num = int(input(f"Elemento {i+1} {j+1}: "))
        linhas.append(num)
    matriz.append(linhas)

maior = matriz[0][0]
menor = matriz[0][0]

for linhas in matriz:
    for num in linhas:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"Maior elemento da matriz: {maior}.")
print(f"Menor elemento da matriz: {menor}.")