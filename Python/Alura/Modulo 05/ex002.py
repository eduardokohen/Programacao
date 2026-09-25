lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

matriz = [lista1, lista2, lista3]

print(matriz)

print(type(matriz))
print(type(lista1))

print(matriz[0][0])
print(matriz[1][2])

matriz[0][1] = 99

print(matriz)

for i, linhas in enumerate(matriz):
    #print(linhas)
    for j, coluna in enumerate(linhas):
        print(f"[{i}][{j}] = {coluna}")