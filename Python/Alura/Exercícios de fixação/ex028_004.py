matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o número da posição [{i} {j}]: "))
        linha.append(numero)
    
    matriz.append(linha)

print("\nMatriz:\n")

for linha in matriz:
    for numero in linha:
        print(numero, end = " ")
    print()