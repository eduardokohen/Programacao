matriz = []
soma = 0

for i in range(3):
    linhas = []
    for j in range(3):
        num = int(input(f"Digite o número da posição [{i+1} {j+1}]: "))
        linhas.append(num)
    matriz.append(linhas)

for linhas in matriz:
    for num in linhas:
        soma += num

print()
print("Matriz:")
print()

for linha in matriz:
    for num in linha:
        print(num, end = " ")
    print()
print(f"A soma de todos elementos da matriz é: {soma}")