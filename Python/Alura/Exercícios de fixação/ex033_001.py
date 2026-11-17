matriz = [
[1, 2, 3],
[4, 5, 6]
]
transposta = [
[matriz[linha][coluna] for linha in range(len(matriz))]
for coluna in range(len(matriz[0]))
]
print(transposta)